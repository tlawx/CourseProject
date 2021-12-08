
class Hospital:

    def __init__(self, hospital_id, name, npi, city=None, state=None, affiliation=None, link="", treatments=None, rating=0):
        self.hospital_id = hospital_id
        self.name = name
        self.npi = npi
        self.city = city
        self.state = state
        self.affiliation = affiliation
        self.link = link
        self.treatments = []

    def __str__(self):
        return "Hospital NPI: {}, Hospital Name: {}".format(self.npi, self.name)

    def __repr__(self):
        return "Hospital NPI: {}, Hospital Name: {}".format(self.npi, self.name)
