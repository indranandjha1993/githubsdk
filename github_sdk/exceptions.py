class InvalidTokenError(Exception):
    """
    Exception raised when an invalid token is used
    """
    pass


class TokenExpiredError(Exception):
    """
    Exception raised when a token has expired
    """
    pass


class ResourceNotFoundError(Exception):
    """
    Exception raised when a resource is not found
    """
    pass


class InvalidRequestError(Exception):
    """
    Exception raised when an invalid request is made
    """
    pass


class RateLimitExceededError(Exception):
    """
    Exception raised when the rate limit is exceeded
    """
    pass


class UnauthorizedError(Exception):
    """
    Exception raised when the request is unauthorized
    """
    pass


class ForbiddenError(Exception):
    """
    Exception raised when the request is forbidden
    """
    pass


class NotAcceptableError(Exception):
    """
    Exception raised when the request is not acceptable
    """
    pass


class ConflictError(Exception):
    """
    Exception raised when a conflict occurs
    """
    pass


class UnprocessableEntityError(Exception):
    """
    Exception raised when the request is unprocessable
    """
    pass


class ServerError(Exception):
    """
    Exception raised when a server error occurs
    """
    pass
