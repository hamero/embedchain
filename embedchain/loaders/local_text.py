class LocalTextLoader:

    def load_data(self, url):
        meta_data = {
            "url": "local",
        }
        if os.path.isfile(url):
            with open(url, 'r') as file:
                content = file.read()
        else:
            # Assuming we have a function named `download_content` to download the content from the url
            content = download_content(url)
        return [{
            "content": content,
            "meta_data": meta_data,
        }]

