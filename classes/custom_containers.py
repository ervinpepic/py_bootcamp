class TagCloud:
    def __init__(self):
        self.__create_tags = {}  # set create_tags to empty dict

    def add(self, add_tag_to_dict):
        self.__create_tags[add_tag_to_dict.lower()] = self.__create_tags.get(
            add_tag_to_dict.lower(), 0) + 1

    def __getitem__(self, get_tag_from_dict):  # this is python function
        return self.__create_tags.get(get_tag_from_dict.lower(), 0)

    def __setitem__(self, set_tag_to_dict, count_of_tags):
        self.__create_tags[set_tag_to_dict.lower()] = count_of_tags

    def __len__(self):
        return len(self.__create_tags)

    def __iter__(self):
        return iter(self.__create_tags)


new_cloud = TagCloud()

new_cloud.add("Python")
new_cloud.add("python")
new_cloud.add("python")
print(new_cloud.__create_tags)
new_cloud["ervin"] = 10
print(new_cloud.__create_tags)
