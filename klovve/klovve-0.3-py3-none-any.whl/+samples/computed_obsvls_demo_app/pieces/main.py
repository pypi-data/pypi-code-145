#  SPDX-FileCopyrightText: © 2022 Josef Hahn
#  SPDX-License-Identifier: AGPL-3.0-only
import threading
import time

import klovve.data
import klovve.pieces.button
import computed_obsvls_demo_app.pieces.mytext


class Model(klovve.Model):

    def __init__(self, **kwargs):  # TODO a mess; and a memleak
        super().__init__(**kwargs)
        def foo():
            while True:
                time.sleep(1)
                self.counter.value += 1 #TODO borken
        threading.Thread(target=foo, daemon=True).start()

    counter = klovve.observable_property(default=lambda: 0)

    @klovve.data.ComputedObservable2(counter=counter)  # TODO what if we use stuff from superclass?
    def label_text(self, counter):  # TODO looks odd without self?!
        return " ".join([digit + chr(0xfe0f) + chr(0x20e3) for digit in str(counter)])


class View(klovve.ComposedView):

    model: Model

    def compose(self, v):
        return pieces.form(
            items=[
                pieces.label(text=self.model.label_text),
                pieces.label(computed_obsvls_demo_app.pieces.mytext.Model()),
            ],
        )
