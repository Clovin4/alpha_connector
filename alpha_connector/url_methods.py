import typing

import logging

import requests

from .urls import FMP_URLS

CONNECT_TIMEOUT = 10
READ_TIMEOUT = 10

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


def __return_json_v3_fmp(path: str, params: dict[str, str]) -> typing.Optional[list]:
    """Return json from the FMP API."""
    fmp = FMP_URLS()
    url = f"{fmp.base_url_v3}{path}"
    return_var = None
    try:
        response = requests.get(
            url, params=params, timeout=(CONNECT_TIMEOUT, READ_TIMEOUT)
        )
        if len(response.content) > 0:
            return_var = response.json()

        if len(response.content) == 0 or (
            isinstance(return_var, dict) and len(return_var.keys()) == 0
        ):
            logging.warning("Response appears to have no data.  Returning empty List.")
            return_var = []

    except requests.Timeout:
        logging.error(f"Connection to {url} timed out.")
    except requests.ConnectionError:
        logging.error(
            f"Connection to {url} failed:  DNS failure, refused connection or some other connection related "
            f"issue."
        )
    except requests.TooManyRedirects:
        logging.error(
            f"Request to {url} exceeds the maximum number of predefined redirections."
        )
    except Exception as e:
        logging.error(
            f"A requests exception has occurred that we have not yet detailed an 'except' clause for.  "
            f"Error: {e}"
        )

    return return_var


def __return_json_v4_fmp(path: str, params: dict[str, str]) -> typing.Optional[list]:
    """Return json from the FMP API."""
    fmp = FMP_URLS()
    url = f"{fmp.base_url_v4}{path}"
    return_var = None
    try:
        response = requests.get(
            url, params=params, timeout=(CONNECT_TIMEOUT, READ_TIMEOUT)
        )
        if len(response.content) > 0:
            return_var = response.json()

        if len(response.content) == 0 or (
            isinstance(return_var, dict) and len(return_var.keys()) == 0
        ):
            logging.warning("Response appears to have no data.  Returning empty List.")
            return_var = []

    except requests.Timeout:
        logging.error(f"Connection to {url} timed out.")
    except requests.ConnectionError:
        logging.error(
            f"Connection to {url} failed:  DNS failure, refused connection or some other connection related "
            f"issue."
        )
    except requests.TooManyRedirects:
        logging.error(
            f"Request to {url} exceeds the maximum number of predefined redirections."
        )
    except Exception as e:
        logging.error(
            f"A requests exception has occurred that we have not yet detailed an 'except' clause for.  "
            f"Error: {e}"
        )

    return return_var


def __validate_time_delta(value: str) -> str:
    """
    Check to see if passed string is in the list of possible Time Deltas.
    :param value: Time Delta name.
    :return: Passed value or No Return
    """
    fmp = FMP_URLS()
    valid_values = fmp.time_delta_values
    if value in valid_values:
        return value
    else:
        logging.error(
            f"Invalid time_delta value: {value}.  Valid options: {valid_values}"
        )
