class PageRequest:
    filtering = "none"
    ordering = "desc"
    page = 1

    def getContext(self, context, filtering, ordering, page):

        
        if filtering == None:
            self.filtering = "none"
        else :
            self.filtering = filtering

        if ordering == None:
            self.ordering = "desc"
        else :
            self.ordering = ordering

        if page == None:
            self.page = 1
        else :
            self.page = page

        context["filter"] = filtering
        context["ordering"] = ordering
        context["page"] = page

        return context
    
    def getParameter(self, filtering, ordering, page):

        if filtering == None:
            self.filtering = "none"
        else :
            self.filtering = filtering

        if ordering == None:
            self.ordering = "desc"
        else :
            self.ordering = ordering

        if page == None:
            self.page = 1
        else :
            self.page = page

        parameter = "?filter={}&ordering={}&page={}".format(self.filtering, self.ordering, self.page)

        return parameter