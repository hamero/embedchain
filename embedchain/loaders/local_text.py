class LocalTextLoader:

    def load_data(self, content):
        import os  # Added import statement for os module
        meta_data = {
            "url": content,
        }
        return [{
            "content": content,
            "meta_data": meta_data,
        }]

