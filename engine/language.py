'''
Decided not to use this. Even for unit 5 the number of words are 152, exeeding 100 chatgpt tokens.
Later implemnet a method to ask for a conversation topic from the UI. that would be enough
07/02/2025
'''


# import spacy
import json
from data_io import Json_IO

class Language():
    def __init__(self):
        self.configuration_data = self.get_configuration_parameters()
        self.JIO = Json_IO(self.configuration_data['database']['database-directory'])
        # self.nlp = spacy.load("es_core_news_sm")


    def get_configuration_parameters(self):
        json_file = "../configuration.json"
        with open(json_file, 'r') as fid:
            json_data = json.load(fid)
        return json_data


    def get_lematized_words(self, words):
        unique_lemmas = list(set(token.lemma_ for token in self.nlp(" ".join(words))))
        return unique_lemmas


    def get_words_for_the_level(self):
        words = self.JIO.get_vocabulary_upto_unit(self.configuration_data['current-unit'], status='all')
        unique_words = list(set(words))
        # unique_lemmas = self.get_lematized_words(unique_words)
        return unique_words


if __name__ == '__main__':
    # lg = Language()
    lg = Language()
    words = lg.get_words_for_the_level()
    print(words)
    print(len(words))
