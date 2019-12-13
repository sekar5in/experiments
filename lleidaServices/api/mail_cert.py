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

from lleidaServices.api import BaseApi, BaseResponse
import os


class MailCertApiResponse(BaseResponse):
    pass


class MailCertApi(BaseApi):
    def __init__(self, config):
        self.endpoint = 'https://tsa.lleida.net/cgi-bin/mailcertapi.cgi'
        super(MailCertApi, self).__init__(**config)

    def get_default_settings(self):
        template_name = 'get_default_settings.xml'
        params = {}
        return self.post(endpoint=self.endpoint, template_name=template_name, in_params=params)

    def set_default_settings(self,
                             mailcert_disabled=None, mailcert_inboxes=None, cert_name = None,
                             cert_name_id = None, cert_lang = None, admin_mail = None, admin_cgi = None,
                             cert_type_subject = None, cert_type_subject_desc = None, enable_from = None,
                             enable_prvs = None, disable_resp_auto = None, send_pdfcpy_from = None,
                             send_pdfcpy_to = None, send_dealpdfcpy_from = None, send_dealpdfcpy_to = None,
                             send_inboxpdfcpy_from = None, send_inboxpdfcpy_to = None, contract_expire_days = None):

        template_name = 'set_default_settings.xml'
        params = {
            'mailcert_disabled': mailcert_disabled, 'mailcert_inboxes': mailcert_inboxes, 'cert_name': cert_name,
            'cert_name_id': cert_name_id, 'cert_lang': cert_lang, 'admin_mail': admin_mail, 'admin_cgi': admin_cgi,
            'cert_type_subject': cert_type_subject, 'cert_type_subject_desc': cert_type_subject_desc,
            'enable_from': enable_from, 'enable_prvs': enable_prvs, 'disable_resp_auto': disable_resp_auto,
            'send_pdfcpy_from': send_pdfcpy_from, 'send_pdfcpy_to': send_pdfcpy_to,
            'send_dealpdfcpy_from': send_dealpdfcpy_from, 'send_dealpdfcpy_to': send_dealpdfcpy_to,
            'send_inboxpdfcpy_from': send_inboxpdfcpy_from, 'send_inboxpdfcpy_to': send_inboxpdfcpy_to,
            'contract_expire_days': contract_expire_days
            }

        response = self.post(endpoint=self.endpoint, template_name=template_name, in_params=params)
        return response

    def list_pdf(self,
                 mail_from=None, mail_to=None,
                 date_min=None, date_max=None,
                 file_id_min=None, file_id_max=None,
                 file_type=None, subjrw=None,
                 mail_id=None, row_order=None,
                 only_last_file_id=False):
        """
        Returns a list of items, each item referencing a Lleida.net email certificante.
        The input parameters act as search criteria to narrow the returned results.

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
        template_name = 'list_pdf.xml'
        params = {
            'mail_from': mail_from, 'mail_to': mail_to,
            'date_min': date_min, 'date_max': date_max,
            'file_id_min': file_id_min, 'file_id_max': file_id_max,
            'file_type': file_type, 'subjrw': subjrw,
            'mail_id': mail_id, 'row_order': row_order,
            'only_last_file_id': only_last_file_id
        }
        response = self.post(endpoint=self.endpoint, template_name=template_name, in_params=params)
        return response

    def download_pdf(self, file_id, custom_path, custom_name):
        """
        Returns the contents of an email certificate PDF file, whose file identifier matches
        the provided input parameter.

        :param file_id: the Lleida.net identifier of the requested PDF file.
        :param custom_name: the Lleida.net identifier of the requested PDF file.
        :return: a MailCertResponse object whose 'content' attribute stores the binary contents of the PDF file.
        """
        if custom_path is None:
            custom_path = '/tmp'
        elif not os.path.exists(custom_path):
            custom_path = '/tmp'

        if custom_name is None:
            custom_name = file_id
        '''
        elif not os.path.exists(os.path.join(custom_path, str(custom_name) + '.pdf')):
            custom_name = file_id
        else:
            custom_name = custom_name
        '''
        # print(custom_name)

        file_download_path = os.path.join(custom_path, str(custom_name) + '.pdf')
        template_name = 'download_pdf.xml'
        params = {'file_id': file_id}

        response = self.post(endpoint=self.endpoint, template_name=template_name, in_params=params)

        if 'content' in response:
            try:
                with open(file_download_path, 'wb') as f:
                    f.write(response['content'])
                return {'action': 'download_pdf', 'status': 100, 'msg': 'success', 'file': file_download_path}
            except Exception as e:
                return {'action': 'download_pdf', 'status': 0, 'msg': e}

        return response
