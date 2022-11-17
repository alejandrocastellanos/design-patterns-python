from structural_patterns.bridge.controllers.implementer.implementer_ios import IOsImplementer


class LinuxImplementer(IOsImplementer):

    def operate_implement(self):
        return 'Linux IOS implementer!'
