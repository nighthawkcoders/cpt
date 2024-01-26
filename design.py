class design:
    def __init__(self,code,likes,dislikes,author,isprivate):
        self.code=code
        self.likes=likes
        self.dislikes=dislikes
        self.author=author
        self.isprivate=isprivate
    def add_like(self):
        self.likes+=1
    def add_dislike(self):
        self.add_dislike+=1
    def remove_like(self):
        self.likes+=1
    
    def remove_dislike(self):
        self.dislikes+=1
    
    def get_isprivate(self):
        return self.isprivate
    
    def get_author(self):
        return self.author
    