# Copyright 2018-2019 Brainbean Apps (https://brainbeanapps.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProjectAssignment(models.Model):
    _name = 'project.assignment'
    _description = 'Project Assignment'
    _inherit = ['mail.thread']

    active = fields.Boolean(
        default=True,
    )
    name = fields.Char(
        compute='_compute_name',
        store=True,
        index=True,
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env['res.company']._company_default_get(),
        ondelete='cascade',
    )
    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project',
        ondelete='cascade',
    )
    role_id = fields.Many2one(
        comodel_name='project.role',
        string='Role',
        required=True,
        ondelete='restrict',
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
        required=True,
        ondelete='restrict',
    )

    _sql_constraints = [
        (
            'project_role_user_uniq',
            'UNIQUE (project_id, role_id, user_id)',
            'User may be assigned per role only once within a project!'
        ),
        (
            'company_role_user_uniq',
            (
                'EXCLUDE ('
                '    company_id WITH =, role_id WITH =, user_id WITH ='
                ') WHERE ('
                '    project_id IS NULL'
                ')'
            ),
            'User may be assigned per role only once within a company!'
        ),
        (
            'nocompany_role_user_uniq',
            (
                'EXCLUDE (role_id WITH =, user_id WITH =) WHERE ('
                '    project_id IS NULL AND company_id IS NULL'
                ')'
            ),
            'User may be assigned per role only once!'
        ),
    ]

    @api.depends(
        'company_id.name',
        'project_id.name',
        'role_id.name',
        'user_id.name',
    )
    def _compute_name(self):
        for assignment in self:
            if assignment.project_id:
                assignment.name = _('%s as %s on %s') % (
                    assignment.user_id.name,
                    assignment.role_id.name,
                    assignment.project_id.name,
                )
            elif assignment.company_id:
                assignment.name = _('%s as %s in %s') % (
                    assignment.user_id.name,
                    assignment.role_id.name,
                    assignment.company_id.name,
                )
            else:
                assignment.name = _('%s as %s') % (
                    assignment.user_id.name,
                    assignment.role_id.name,
                )

    @api.multi
    def _get_conflicting_domain(self):
        self.ensure_one()
        return [
            ('id', '!=', self.id),
            ('role_id', '=', self.role_id.id),
            ('user_id', '=', self.user_id.id),
        ] + (
            [('company_id', 'in', [False, self.company_id.id])]
            if self.company_id else []
        ) + (
            [('project_id', 'in', [False, self.project_id.id])]
            if self.project_id else []
        )

    @api.multi
    @api.constrains('company_id', 'project_id', 'role_id', 'user_id')
    def _check(self):
        """
        Check if assignment conflicts with any already-existing assignment and
        if specific role can be assigned at all (extension hook).
        """
        for assignment in self:
            conflicting_assignment = self.search(
                assignment._get_conflicting_domain(),
                limit=1,
            )
            if conflicting_assignment:
                raise ValidationError(_(
                    'Assignment %s conflicts with another assignment: %s'
                ) % (
                    assignment.name,
                    conflicting_assignment.name,
                ))
            if not assignment.role_id.can_assign(
                    assignment.user_id, assignment.project_id):
                if assignment.project_id:
                    error = _(
                        'User %s can not be assigned to role %s on %s.'
                    ) % (
                        assignment.user_id.name,
                        assignment.role_id.name,
                        assignment.project_id.name,
                    )
                else:
                    error = _(
                        'User %s can not be assigned to role %s.'
                    ) % (
                        assignment.user_id.name,
                        assignment.role_id.name,
                    )
                raise ValidationError(error)
