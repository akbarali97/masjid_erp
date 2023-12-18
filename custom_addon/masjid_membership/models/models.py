# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MasjidMembership(models.Model):
    _name = 'masjid_membership.masjid_membership'
    _description = 'masjid_membership.masjid_membership'

    GENDER_SELECTION = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    membership_number = fields.Integer(string=_("Membership Number"), required=True)
    name = fields.Char(string=_("Name"), required=True)
    gender = fields.Selection(GENDER_SELECTION, string='Gender', required=True)

    date_of_birth = fields.Date(string=_("Name"))

    surname = fields.Many2one('masjid_membership.surname_record')
    address = fields.Text(string=_("Address"))
    locality = fields.Char(string=_("Panchayat/Muncipality"))

    father_name = fields.Char(string=_("Father's Name"))
    mother_name = fields.Char(string=_("Mother's Name"))

    grand_father_name = fields.Char(string=_("Grand Father's Name"))
    grand_mother_name = fields.Char(string=_("Grand Mother's Name"))

    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100


class LineageRecord(models.Model):
    _name = 'masjid_membership.lineage_record'


    RELATION_SELECTION = [
        ('father', _("Father")),
        ('mother', _("Mother")),
        ('brother', _("Brother")),
        ('sister', _("Sister")),
        ('grand_father', _("Grand Father")),
        ('grand_mother', _("Grand Mother")),
        ('uncle', _("Uncle")),
    ]

    name = fields.Char(string=_("Name"), required=True)
    relation = fields.Selection(RELATION_SELECTION, string='relation', required=True)

class SurnameRecord(models.Model):
    _name = 'masjid_membership.surname_record'

    name = fields.Char(string=_("Surname"))