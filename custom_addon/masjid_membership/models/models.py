# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api, _


class Membership(models.Model):
    _name = 'masjid_membership.membership'
    _description = 'Membership'

    member = fields.Many2one('masjid_membership.member', string=_("Membership Holder"), required=True, domain="[('id', 'in', filter_membership_holder)]")
    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)
    membership_number = fields.Integer(string=_("Membership Number"), required=True)
    house_number = fields.Integer(string=_("House Number"), required=True)
    house_name = fields.Char(string=_("House Name"), required=True, default=lambda self: self.member.surname.name)
    ward_number = fields.Integer(string=_("Ward Number"), required=True)
    address = fields.Text(string=_("Address"))
    locality = fields.Char(string=_("Locality"), default='Kanippayyur')
    joined_on = fields.Date(string=_("Joined on"), required=True)

    relationships = fields.Many2many(
        comodel_name='masjid_membership.relationship',
        relation='masjid_membership_relationship_items',
        string=_("Relationships"))

    filter_membership_holder = fields.Many2many(
        'masjid_membership.member', 
        compute='_compute_filter_membership_holder',
        invisible=True)

    existing_dependants = fields.Many2many(
        comodel_name='masjid_membership.member',
        compute='_compute_existing_dependants',
        string=_("Existing Dependants"),
        readonly=True)

    @api.depends('member', 'house_number')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.member.display_name} - {record.membership_number}"

    @api.onchange('member')
    def member_on_change(self):
        self.house_name = self.member.surname.name

    def _compute_filter_membership_holder(self):
        for record in self:
            dependant_members = self.env['masjid_membership.relationship'].search([
                ('is_dependant', '=', False)]).mapped('person')
            record.filter_membership_holder = [(6, 0, dependant_members.ids)]

    @api.depends('relationships', 'relationships.person')
    def _compute_existing_dependants(self):
        for record in self:
            if record.relationships:
                record.existing_dependants = record.relationships.mapped('person')
            else:
                record.existing_dependants = False

class MemberDetails(models.Model):
    _name = 'masjid_membership.member'
    _description = 'Member'

    GENDER_SELECTION = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = fields.Char(string=_("Name"), required=True)
    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)
    mobile = fields.Char(string=_("Mobile"), required=True)
    gender = fields.Selection(GENDER_SELECTION, string=_("Gender"), required=True)
    date_of_birth = fields.Date(string=_("Date of Birth"))
    age = fields.Integer(string=_('Age'), compute='_compute_age', store=False)
    surname = fields.Many2one('masjid_membership.surname', string=_("Surname"), required=True)
    job = fields.Many2one('masjid_membership.job', string=_("Job"), required=False)
    job_country = fields.Many2one('masjid_membership.job_country', string=_("Job Country"), required=False)
    education = fields.Many2one('masjid_membership.education', string=_("Education"), required=False)
    marital_status = fields.Many2one('masjid_membership.marital_status', 
                                     string=_("Marital Status"), 
                                     required=False)
    diseases = fields.Many2many(
        comodel_name='masjid_membership.disease', 
        relation='masjid_membership_diseases_items', 
        string=_("Diseases"), 
        required=False)
    date_of_death = fields.Date(string=_("Date of Death"))
    graveyard = fields.Many2one('masjid_membership.graveyard', string=_("Graveyard"), required=False)

    @api.depends('name', 'surname')
    def _compute_display_name(self):
        for record in self:
            record.display_name = f"{record.surname.name} {record.name}"

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth:
                rec.age = date.today().year - rec.date_of_birth.year
            else:
                rec.age = 0