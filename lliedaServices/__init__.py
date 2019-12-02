# -*- coding: utf-8 -*-
# Title           :lliedaClient.py
# Description     :This will create a header for a python script.
# Author          :Dhanasekara Pandian
# Email           :dhana.s@contecuae.com
# Date            :20191202
# Version         :0.1
# Usage           :python lliedaClient.py
# Notes           :This is proprietary software of i2i Telesource India Pvt Ltd.
# Python_version  :3.6

from .api.mail_cert import MailCertApi


class PyLleida(object):
    def __init__(self, username, password):
        """
        Python wrapper for the Lleida.net API.

        There exists only one way to authenticate with the Lleida.net API, which consists on providing a
        username/password combination.

        :param username: Lleida.net username
        :param password: Lleida.net password
        """

        config = dict(
            username=username,
            password=password
        )
        self.mailcert = MailCertApi(config)

    def get_default_settings(self):
       """
       Python wrapper for the Lleida.net API.

       There exists only one way to authenticate with the Lleida.net API, which consists on providing a
       username/password combination.

       :param username: Lleida.net username
       :param password: Lleida.net password
       """
       return self.mailcert.get_default_settings()

    def set_default_settings(self,
                             mailcert_disabled=None, mailcert_inboxes=None, cert_name = None,
                             cert_name_id = None, cert_lang = None, admin_mail = None, admin_cgi = None,
                             cert_type_subject = None, cert_type_subject_desc = None, enable_from = None,
                             enable_prvs = None, disable_resp_auto = None, send_pdfcpy_from = None,
                             send_pdfcpy_to = None, send_dealpdfcpy_from = None, send_dealpdfcpy_to = None,
                             send_inboxpdfcpy_from = None, send_inboxpdfcpy_to = None, contract_expire_days = None):
        """
        Python wrapper for the Lleida.net API.

        There exists only one way to authenticate with the Lleida.net API, which consists on providing a
        username/password combination.

        :param contract_expire_days: It can be used to specify the maximum number of days to finish a contract.
                Once exceeded it will expire. If 0 is used, the default value of 31 days will be used.
                Values between 3 and 30, both included, can be used. Values above 30 will be considered as 30,
                and values below 3 will be considered as 3.
        :param send_inboxpdfcpy_to: Flag: 0 or 1. 1 to send a recpetion document copy to the principal address
                admin_mail. 0 to deactivate.
        :param send_inboxpdfcpy_from: Flag: 0 or 1. 1 to send a reception document copy to origin. 0 to deactivate.
        :param send_dealpdfcpy_to: Flag: 0 or 1. 1 to send a contract document copy to the addressee. 0 to deactivate.
        :param send_dealpdfcpy_from: Flag: 0 or 1. 1 to send a contract document copy to origin. 0 to deactivate.
        :param send_pdfcpy_to: Flag: 0 or 1. 1 to send a mail document copy to the addressee. 0 to deactivate.
        :param send_pdfcpy_from: Flag: 0 or 1. 1 to send a mail document copy to origin. 0 to deactivate.
        :param disable_resp_auto: Flag: 0 or 1. 1 to deactivate automatic notifications. 0 by default.
        :param enable_prvs: Flag: 0 or 1. 1 to activate the compatibility with return addresses that use BATV or
               PRVS format. 0 by default.
        :param enable_from: Flag: 0 or 1. 1 to activate additional validation for the from field against the whitelist.
        :param cert_type_subject_desc:
        :param cert_type_subject: The code associated to the type of document to be generated depending on the
               subject of the registered email.
        :param admin_cgi: URL address where you wish to received all generated events. It includes the following
               variables: eventid, eventdate, eventname, rcode and b64info.
        :param admin_mail: Email address where you wish to recive all the generated documents.
        :param cert_lang: Certified documents language.
        :param cert_name_id: Certificate name reference id
        :param cert_name: Certificate name
        :param mailcert_inboxes: No of inboxes for the requested credentials.
        :param mailcert_disabled: NO or YES (NO by default).
        :param username: Lleida.net username
        :param password: Lleida.net password
        :return: a JSON response containing the results.
        """
        return self.mailcert.set_default_settings(mailcert_disabled=mailcert_disabled, mailcert_inboxes=mailcert_inboxes,
                                                  cert_name = cert_name, cert_name_id = cert_name_id, cert_lang = cert_lang,
                                                  admin_mail = admin_mail, admin_cgi = admin_cgi,
                                                  cert_type_subject = cert_type_subject,
                                                  cert_type_subject_desc=cert_type_subject_desc, enable_from=enable_from,
                                                  enable_prvs = enable_prvs, disable_resp_auto = disable_resp_auto,
                                                  send_pdfcpy_from = send_pdfcpy_from, send_pdfcpy_to = send_pdfcpy_to,
                                                  send_dealpdfcpy_from = send_dealpdfcpy_from,
                                                  send_dealpdfcpy_to = send_dealpdfcpy_to,
                                                  send_inboxpdfcpy_from = send_inboxpdfcpy_from,
                                                  send_inboxpdfcpy_to = send_inboxpdfcpy_to,
                                                  contract_expire_days = contract_expire_days)

    def list_pdf(self, mail_from=None, mail_to=None, date_min=None, date_max=None, file_id_min=None, file_id_max=None,
                 file_type=None, subjrw=None, mail_id=None, row_order=None, only_last_file_id=False):
        """
        Python wrapper for the Lleida.net API.

        There exists only one way to authenticate with the Lleida.net API, which consists on providing a
        username/password combination.

        :param mail_from: results by a given sender's email address.
        :param mail_to: filter results by a given recipient's email address.
        :param date_min: filter results starting from an initial date.
        :param date_max: filter results starting from a final date.
        :param file_id_min: filter results starting from a minimum file_id.
        :param file_id_max: filter results up to a maximum file_id.
        :param file_type: filter results by the file/document type.
        :param subjrw: filter results based on a substring that appears in the emails' subjects. It is advised to
        use ASCII alphanumeric values that may appear in the first 200 character positions of the subject.
        :param mail_id: filter results by the mail id of an email certificate.
        :param row_order: filter results by ascending or descending order based on the email certificate id.
        Valid values are 'asc' for ascending order, 'desc' for descending order.
        :param only_last_file_id: return a single element, (the latest email certificate file identifier)
        in the response.
        :return: a JSON response containing the results.
        """
        return self.mailcert.list_pdf(mail_from=mail_from, mail_to=mail_to, date_min=date_min, date_max=date_max,
                                      file_id_min=file_id_min, file_id_max=file_id_max, file_type=file_type,
                                      subjrw=subjrw, mail_id=mail_id, row_order=row_order,
                                      only_last_file_id=only_last_file_id)

    def download_pdf(self, file_id, custom_path=None, custom_name=None):
        """
        Python wrapper for the Lleida.net API.

        There exists only one way to authenticate with the Lleida.net API, which consists on providing a
        username/password combination.

        :param file_id: generated file number for specific document
        :param custom_path: custom path for pdf document download
        :param custom_name: custom name for pdf document download
        :param username: Lleida.net username
        :param password: Lleida.net password
        """
        return self.mailcert.download_pdf(file_id, custom_path, custom_name)


