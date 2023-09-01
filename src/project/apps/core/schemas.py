from project.extensions import ma


class PaginationSchema(ma.Schema):
    currentPage = ma.String()
    hasNext = ma.Boolean()
    hasPrev = ma.Boolean()
    pages = ma.Integer()
    size = ma.Integer()
    totalElements = ma.Integer()
