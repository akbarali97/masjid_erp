# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Relation(models.Model):
    _name = 'masjid_membership.relation'
    _description = 'Relation'

    name = fields.Char(string=_("Relation"))



class Relationship(models.Model):
    _name = 'masjid_membership.relationship'
    _description = 'Relationship'

    relation = fields.Many2one('masjid_membership.relation', string=_("Relation"), required=False)
    person = fields.Many2one('masjid_membership.member', string=_("dependant"), required=False)



class Surname(models.Model):
    _name = 'masjid_membership.surname'
    _description = 'Surname'

    name = fields.Char(string=_("Surname"))



class Education(models.Model):
    _name = 'masjid_membership.education'
    _description = 'Education'

    name = fields.Char(string=_("Education"))



class Job(models.Model):
    _name = 'masjid_membership.job'
    _description = 'Job'

    name = fields.Char(string=_("Job"))



class JobCountry(models.Model):
    _name = 'masjid_membership.job_country'
    _description = 'Job Country'

    name = fields.Char(string=_("Country"))



class MaritalStatus(models.Model):
    _name = 'masjid_membership.marital_status'
    _description = 'Marital Status'

    name = fields.Char(string=_("Marital Status"))



class Disease(models.Model):
    _name = 'masjid_membership.disease'
    _description = 'Diseases'

    name = fields.Char(string=_("Disease"))



class Graveyard(models.Model):
    _name = 'masjid_membership.graveyard'
    _description = 'Job Country'

    name = fields.Char(string=_("Graveyard"))