from app.domain.enums.error_codes import ErrorCode

class BusinessException(Exception):
    def __init__(self, code: ErrorCode):
        self.code = code
        self.message = code.value
        super().__init__(self.message)
