from structural_patterns.bridge.controllers.implementer.implementer_ios import IOsImplementer


class WindowsImplementer(IOsImplementer):

    def operate_implement(self):
        return 'Windows IOS implementer!'
