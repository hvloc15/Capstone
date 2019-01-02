from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

def core_exception_handler(exc, context):
    # If an exception is thrown that we don't explicitly handle here, we want
    # to delegate to the default exception handler offered by DRF. If we do
    # handle this exception type, we will still want access to the response
    # generated by DRF, so we get that response up front.
    response = exception_handler(exc, context)
    handlers = {
        'NotFound': _handle_not_found_error,
        'ValidationError': _handle_generic_error,
    }
    # This is how we identify the type of the current exception. We will use
    # this in a moment to see whether we should handle this exception or let
    # Django REST Framework do it's thing.
    exception_class = exc.__class__.__name__

    return handlers.get(exception_class,_default_error)(exc, context, response)

def _default_error(exc, context, response):
    return Response({"errors":str(exc)}, status=HTTP_400_BAD_REQUEST)

def _handle_generic_error(exc, context, response):
    # This is about the most straightforward exception handler we can create.
    # We take the response generated by DRF and wrap it in the `errors` key.

    response.data = {
        'errors': response.data
    }

    return response

def _handle_not_found_error(exc, context, response):
    view = context.get('view', None)

    if view and hasattr(view, 'queryset') and view.queryset is not None:
        error_key = view.queryset.model._meta.verbose_name

        response.data = {
            'errors': {
                error_key: response.data['detail']
            }
        }

    else:
        response = _handle_generic_error(exc, context, response)

    return response
