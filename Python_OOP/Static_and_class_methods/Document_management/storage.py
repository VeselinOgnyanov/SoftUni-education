from category import Category
from document import Document
from topic import Topic


class Storage:
    @staticmethod
    def filtering(id_to_filter, list_to_filter_from):
        filtered_category = list(filter(lambda object_to_filter: (object_to_filter.id == id_to_filter)
                                        , list_to_filter_from))[0]
        return filtered_category

    def __init__(self) -> None:
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        #this is converted to list, so when used, take the first element filtered_category[0]
        #category = [c for c in self.categories if c.id == category_id][0]
        filtered_category = self.filtering(id_to_filter= category_id, list_to_filter_from= self.categories)

        if filtered_category:
            filtered_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        filtered_topic = list(filter(lambda object: (object.id == topic_id), self.topics))[0]
        if filtered_topic:
            filtered_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        filtered_document = list(filter(lambda object: (object.id == document_id), self.documents))[0]
        if filtered_document:
            filtered_document.edit(new_file_name)

    def delete_category(self, category_id):
        filtered_category = list(filter(lambda object: (object.id == category_id), self.categories))[0]
        if filtered_category:
            self.categories.remove(filtered_category)

    def delete_topic(self, topic_id):
        filtered_topic = list(filter(lambda object: (object.id == topic_id), self.topics))[0]
        if filtered_topic:
            self.topics.remove(filtered_topic)

    def delete_document(self, document_id):
        filtered_document = list(filter(lambda object: (object.id == document_id), self.documents))[0]
        if filtered_document:
            self.documents.remove(filtered_document)

    def get_document(self, document_id):
        filtered_document = list(filter(lambda object: (object.id == document_id), self.documents))[0]
        if filtered_document:
            return filtered_document

    def __repr__(self):
        list_to_print = []

        for element in self.documents:
            list_to_print.append(element)

        str_to_print = [str(x) for x in list_to_print]
        return ', '.join(str_to_print)
