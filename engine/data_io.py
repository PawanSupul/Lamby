import json
import os
import warnings


class Json_IO():
    def __init__(self, vocabulary_json_directory):
        self.vocabulary_json_directory = vocabulary_json_directory


    def read_json_file(self, unit: int) -> dict:
        json_file = os.path.join(self.vocabulary_json_directory, f'unit_{unit}.json')
        with open(json_file, 'r', encoding='utf-8') as fid:
            json_data = json.load(fid)
        return json_data


    def get_subunit_lesson_list(self, vocabulary_list: list, subunit_id: str ='all', status: str ='all') -> list:
        lesson_list = []
        sub_id_list = []
        lesson_available = False
        for i in range(len(vocabulary_list)):
            temp_dic = vocabulary_list[i]
            sub_id = temp_dic['sub-id']
            sub_id_list.append(sub_id)
            if(subunit_id != 'all'):                                # otherwise use "2-1" etc
                # read only a single subunit
                if(sub_id == subunit_id):
                    return temp_dic['lesson']
            else:
                subunit_status = temp_dic['status']
                if(status != 'all'):                                # otherwise use "REVIEWED" etc
                    # read only reviewed/introduced subunits
                    if(subunit_status == status):
                        lesson_list.extend(temp_dic['lesson'])
                        lesson_available = True
                else:
                    # read all subunits
                    lesson_list.extend(temp_dic['lesson'])
                    lesson_available = True
        # Set warnings
        if(subunit_id != 'all'):
            if (status != 'all'):
                warnings.warn('WARNING: Subunit-id specified. Status of the subunits are ignored!')
            if (subunit_id not in sub_id_list):
                warnings.warn('WARNING: Specified subunit does not exist! Returning an empty list.')
        else:
            if (status != 'all' and lesson_available == False):
                warnings.warn('WARNING: Specified STATUS is not available for this unit!')
        return lesson_list


    def get_vocabulary_of_unit(self, unit: int, subunit_id: str = 'all', status: str = 'all') -> list[str]:
        json_data = self.read_json_file(unit)
        vocabulary_list = json_data['vocabulary']
        lesson_list = self.get_subunit_lesson_list(vocabulary_list, subunit_id=subunit_id, status=status)
        vocabulary = []
        for i in range(len(lesson_list)):
            words = lesson_list[i]['words']
            vocabulary.extend(words)
        unique_vocabulary = list(set(vocabulary))
        return unique_vocabulary


    def get_vocabulary_upto_unit(self, max_unit, status='all'):
        unit_list = [x for x in range(1, max_unit+1)]
        vocabulary = []
        for unit in unit_list:
            unit_vocabulary = self.get_vocabulary_of_unit(unit, 'all', status=status)
            vocabulary.extend(unit_vocabulary)
        unique_vocabulary = list(set(vocabulary))
        return unique_vocabulary


if __name__ == '__main__':
    vocabulary_json_directory = r'tests/'
    jio = Json_IO(vocabulary_json_directory)
    unique_words = jio.get_vocabulary_upto_unit(2, 'all')
    print(set(unique_words))
