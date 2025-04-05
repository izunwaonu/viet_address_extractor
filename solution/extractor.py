
# import os
# from trie.trie import Trie

# # ✅ Normalization mappings
# def normalize(name, mapping):
#     return mapping.get(name.lower(), name)

# same_province = {
#     "hcm": "Hồ Chí Minh", "tp hcm": "Hồ Chí Minh", "tp. hcm": "Hồ Chí Minh",
#     "sài gòn": "Hồ Chí Minh", "ho chi minh": "Hồ Chí Minh", "hồ chí minh": "Hồ Chí Minh",
#     "hn": "Hà Nội", "tp hn": "Hà Nội", "tp. hn": "Hà Nội", "ha noi": "Hà Nội",
# }

# same_district = {
#     "q1": "Quận 1", "quan 1": "Quận 1", "quận 1": "Quận 1",
#     "q2": "Quận 2", "quan 2": "Quận 2", "quận 2": "Quận 2",
#     "q3": "Quận 3", "quan 3": "Quận 3", "quận 3": "Quận 3",
#     "thủ đức": "Thành phố Thủ Đức", "thu duc": "Thành phố Thủ Đức",
#     "binh thanh": "Quận Bình Thạnh", "bình thạnh": "Quận Bình Thạnh",
#     "go vap": "Quận Gò Vấp", "gò vấp": "Quận Gò Vấp",
#     "tan binh": "Quận Tân Bình", "tân bình": "Quận Tân Bình",
# }

# same_ward = {
#     "p1": "Phường 1", "phuong 1": "Phường 1", "phường 1": "Phường 1",
#     "p2": "Phường 2", "phuong 2": "Phường 2", "phường 2": "Phường 2",
#     "p3": "Phường 3", "phuong 3": "Phường 3", "phường 3": "Phường 3",
#     "p.13": "Phường 13", "phuong 13": "Phường 13",
#     "thảo điền": "Phường Thảo Điền", "thao dien": "Phường Thảo Điền",
#     "tân định": "Phường Tân Định", "tan dinh": "Phường Tân Định",
# }

# class Solution:
#     def __init__(self):
#         # Initialize tries for each level
#         self.province_trie = Trie()
#         self.district_trie = Trie()
#         self.ward_trie = Trie()

#         # Load data
#         self.provinces = self.load_data("data/list_province.txt")
#         self.districts = self.load_data("data/list_district.txt")
#         self.wards = self.load_data("data/list_ward.txt")

#         # Insert into tries
#         for p in self.provinces:
#             self.province_trie.insert(p)
#         for d in self.districts:
#             self.district_trie.insert(d)
#         for w in self.wards:
#             self.ward_trie.insert(w)

#     def load_data(self, path):
#         if not os.path.exists(path):
#             print(f"File not found: {path}")
#             return []
#         with open(path, "r", encoding="utf-8") as f:
#             return [line.strip() for line in f]

#     def process(self, s: str):
#         s = s.lower()

#         province = self.province_trie.search_longest(s)
#         district = self.district_trie.search_longest(s)
#         ward = self.ward_trie.search_longest(s)

#         return {
#             "province": province,
#             "district": district,
#             "ward": ward
#         }


import os
from trie.trie import Trie

# ✅ Normalization mappings
def normalize(name, mapping):
    name = name.lower().strip()
    return mapping.get(name, name)

same_province = {
    "hcm": "Hồ Chí Minh", "tp hcm": "Hồ Chí Minh", "tp. hcm": "Hồ Chí Minh",
    "sài gòn": "Hồ Chí Minh", "ho chi minh": "Hồ Chí Minh", "hồ chí minh": "Hồ Chí Minh",
    "hn": "Hà Nội", "tp hn": "Hà Nội", "tp. hn": "Hà Nội", "ha noi": "Hà Nội",
}

same_district = {
    "q1": "Quận 1", "quan 1": "Quận 1", "quận 1": "Quận 1",
    "q2": "Quận 2", "quan 2": "Quận 2", "quận 2": "Quận 2",
    "q3": "Quận 3", "quan 3": "Quận 3", "quận 3": "Quận 3",
    "thủ đức": "Thành phố Thủ Đức", "thu duc": "Thành phố Thủ Đức",
    "binh thanh": "Quận Bình Thạnh", "bình thạnh": "Quận Bình Thạnh",
    "go vap": "Quận Gò Vấp", "gò vấp": "Quận Gò Vấp",
    "tan binh": "Quận Tân Bình", "tân bình": "Quận Tân Bình",
}

same_ward = {
    "p1": "Phường 1", "phuong 1": "Phường 1", "phường 1": "Phường 1",
    "p2": "Phường 2", "phuong 2": "Phường 2", "phường 2": "Phường 2",
    "p3": "Phường 3", "phuong 3": "Phường 3", "phường 3": "Phường 3",
    "p.13": "Phường 13", "phuong 13": "Phường 13",
    "thảo điền": "Phường Thảo Điền", "thao dien": "Phường Thảo Điền",
    "tân định": "Phường Tân Định", "tan dinh": "Phường Tân Định",
}

class Solution:
    def __init__(self):
        # Initialize tries for each level
        self.province_trie = Trie()
        self.district_trie = Trie()
        self.ward_trie = Trie()

        # Load data
        self.provinces = self.load_data("data/list_province.txt")
        self.districts = self.load_data("data/list_district.txt")
        self.wards = self.load_data("data/list_ward.txt")

        # Insert into tries
        for p in self.provinces:
            self.province_trie.insert(p)
        for d in self.districts:
            self.district_trie.insert(d)
        for w in self.wards:
            self.ward_trie.insert(w)

    def load_data(self, path):
        if not os.path.exists(path):
            print(f"File not found: {path}")
            return []
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]

    def process(self, s: str):
        s = s.lower()

        # Normalize first
        s = normalize(s, same_province)
        s = normalize(s, same_district)
        s = normalize(s, same_ward)

        # Get all matches
        ward_matches = self.ward_trie.search_all_longest(s)
        district_matches = self.district_trie.search_all_longest(s)
        province_matches = self.province_trie.search_all_longest(s)

        # Select longest match from each list (if any)
        ward = max(ward_matches, key=lambda x: len(x[2]), default=(0, 0, ""))[2]
        district = max(district_matches, key=lambda x: len(x[2]), default=(0, 0, ""))[2]
        province = max(province_matches, key=lambda x: len(x[2]), default=(0, 0, ""))[2]

        return {
            "province": province,
            "district": district,
            "ward": ward
        }
