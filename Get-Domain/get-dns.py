
# pip3 install python-whois
import whois
domain = input("Enter the domain : ")
domain_info = whois.whois(domain)

for key,value in domain_info.items():
	print(key,":", value)

  
  
'''
python3 get-dns.py
Enter the domain : yahoo.com
domain_name : ['YAHOO.COM', 'yahoo.com']
registrar : MarkMonitor, Inc.
whois_server : whois.markmonitor.com
referral_url : None
updated_date : [datetime.datetime(2022, 3, 9, 21, 10, 9), datetime.datetime(2022, 3, 9, 15, 51, 45, tzinfo=datetime.timezone.utc)]
creation_date : [datetime.datetime(1995, 1, 18, 5, 0), datetime.datetime(1995, 1, 18, 8, 0, tzinfo=datetime.timezone.utc)]
expiration_date : [datetime.datetime(2023, 1, 19, 5, 0), datetime.datetime(2023, 1, 19, 5, 0, tzinfo=datetime.timezone.utc)]
name_servers : ['NS1.YAHOO.COM', 'NS2.YAHOO.COM', 'NS3.YAHOO.COM', 'NS4.YAHOO.COM', 'NS5.YAHOO.COM', 'ns1.yahoo.com', 'ns5.yahoo.com', 'ns3.yahoo.com', 'ns2.yahoo.com', 'ns4.yahoo.com']
status : ['clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited', 'clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited', 'serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited', 'serverTransferProhibited https://icann.org/epp#serverTransferProhibited', 'serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited', 'clientUpdateProhibited (https://www.icann.org/epp#clientUpdateProhibited)', 'clientTransferProhibited (https://www.icann.org/epp#clientTransferProhibited)', 'clientDeleteProhibited (https://www.icann.org/epp#clientDeleteProhibited)', 'serverUpdateProhibited (https://www.icann.org/epp#serverUpdateProhibited)', 'serverTransferProhibited (https://www.icann.org/epp#serverTransferProhibited)', 'serverDeleteProhibited (https://www.icann.org/epp#serverDeleteProhibited)']
emails : ['abusecomplaints@markmonitor.com', 'whoisrequest@markmonitor.com']
dnssec : unsigned
name : None
org : Yahoo Assets LLC
address : None
city : None
state : VA
registrant_postal_code : None
country : US
'''
