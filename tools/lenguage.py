from translate import Translator


class Translate:

    def convert(self, text):
        translator = Translator(to_lang="German")
        translation = translator.translate(text)
        return translation
