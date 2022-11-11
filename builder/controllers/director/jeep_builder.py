from builder.controllers.builder.builder import Builder


class JeepBuilder:

    _builder = None

    def set_builder(self, builder: Builder):
        self._builder = builder

    def create_jeep(self):
        self._builder.set_wheel_parameters(30).set_engine_parameters(1200).set_body_parameters('PICKUP')
        return self._builder.build()
