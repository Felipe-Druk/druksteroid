import pickle



class Savior:

    def __init__(self, file_name):
        self._datos = None
        self._file_name = file_name

    def serialize(self):
        with open(self._file_name, 'wb') as f:
            pickle.dump(self._datos, f)

    def deserialize(self):
        try:
            with open(self._file_name, 'rb') as f:
                loded_data = pickle.load(f)
                return loded_data
        except FileNotFoundError: 
            return None