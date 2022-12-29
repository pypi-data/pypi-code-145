#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import klovve


class Model(klovve.Model):

    item = klovve.Property()

    label = klovve.Property(default=lambda: "")


class View(klovve.BaseView):

    model: Model
