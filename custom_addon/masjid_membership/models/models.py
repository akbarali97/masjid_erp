# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MasjidMembership(models.Model):
    _name = 'masjid_membership.masjid_membership'
    _description = 'masjid_membership.masjid_membership'


    membership_number = fields.Integer(string=_("Membership Number"))
    name = fields.Char(string=_("Name"))
    gender = fields.Selection()
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

    name = fields.Char(string=_("Name"))
    relation = fields.Selection(_(""))

class SurnameRecord(models.Model):
    _name = 'masjid_membership.surname_record'

    name = fields.Char(string=_("Surname"))