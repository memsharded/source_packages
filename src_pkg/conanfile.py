from conans import ConanFile


class SourcesConan(ConanFile):
    exports_sources = "src/*"

    def package(self):
        self.copy("*")

