#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    This file is part of parltrack

#    parltrack is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    parltrack is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with parltrack  If not, see <http://www.gnu.org/licenses/>.

# (C) 2011 by Stefan Marsiske, <stefan.marsiske@gmail.com>, Asciimoo

COMMITTEE_MAP={u'AFET': u"Foreign Affairs",
               u'DROI': u"Human Rights",
               u'CLIM': u'Climate Change',
               u'CRIM': u'Organised crime, corruption and money laundering',
               u'TDIP': u'Temporary committee on use of European countries by the CIA',
               u'SEDE': u"Security and Defence",
               u'DEVE': u"Development",
               u'INTA': u"International Trade",
               u'BUDG': u"Budgets",
               u'CONT': u"Budgetary Control",
               u'CODE': u"Conciliation Committee",
               u'ECON': u"Economic and Monetary Affairs",
               u'EMPL': u"Employment and Social Affairs",
               u'ENVI': u"Environment, Public Health and Food Safety",
               u'ITRE': u"Industry, Research and Energy",
               u'IMCO': u"Internal Market and Consumer Protection",
               u'TRAN': u"Transport and Tourism",
               u'REGI': u"Regional Development",
               u'AGRI': u"Agriculture and Rural Development",
               u'PECH': u"Fisheries",
               u'CULT': u"Culture and Education",
               u'JURI': u"Legal Affairs",
               u'LIBE': u"Civil Liberties, Justice and Home Affairs",
               u'AFCO': u"Constitutional Affairs",
               u'FEMM': u"Women's Rights and Gender Equality",
               u'PETI': u"Petitions",
               u'CRIS': u"Financial, Economic and Social Crisis",
               u'SURE': u"Policy Challenges Committee",
               u'RETT': u"Regional Policy, Transport and Tourism",
               u'Foreign Affairs': u'AFET',
               u"Regional Policy, Transport and Tourism": u'RETT',
               u'Foreign Affairs': u'AFET',
               u'Human Rights': u'DROI',
               u'Security and Defence': u'SEDE',
               u'Development': u'DEVE',
               u'International Trade': u'INTA',
               u'Budgets': u'BUDG',
               u'Budgetary Control': u'CONT',
               u'Organised crime, corruption and money laundering' : u'CRIM',
               u'Economic and Monetary Affairs': u'ECON',
               u'Employment and Social Affairs': u'EMPL',
               u'Environment, Public Health and Food Safety': u'ENVI',
               u'Industry, Research and Energy': u'ITRE',
               u'Internal Market and Consumer Protection': u'IMCO',
               u'Transport and Tourism': u'TRAN',
               u'Regional Development': u'REGI',
               u'Agriculture and Rural Development': u'AGRI',
               u'Fisheries': u'PECH',
               u'Culture and Education': u'CULT',
               u'Legal Affairs': u'JURI',
               u'Civil Liberties, Justice and Home Affairs': u'LIBE',
               u'Constitutional Affairs': u'AFCO',
               u"Women's Rights and Gender Equality": u'FEMM',
               u"Committee on Women's Rights and Gender": u'FEMM',
               u"Women’s Rights and Gender Equality": u'FEMM',
               u'Petitions': u'PETI',
               u'Financial, Economic and Social Crisis': u'CRIS',
               u'Policy Challenges Committee': u'SURE',
               u'Committee on Foreign Affairs': u'AFET',
               u'Committee on Human Rights': u'DROI',
               u'Committee on Security and Defence': u'SEDE',
               u'Committee on Development': u'DEVE',
               u'Committee on development': u'DEVE',
               u'Special Committee on the Financial, Economic and Social Crisis': u'CRIS',
               u'Special committee on the policy challenges and budgetary resources for a sustainable': u'SURE',
               u'Special committee on the policy challenges and budgetary resources for a sustainable European Union after 2013': u'SURE',
               u'Committee on International Trade': u'INTA',
               u'Committee on Budgets': u'BUDG',
               u'Committee on Budgetary Control': u'CONT',
               u'Committee on Economic and Monetary Affairs': u'ECON',
               u'Committee on Employment and Social Affairs': u'EMPL',
               u"Commission de l'emploi et des affaires sociales": u'EMPL',
               u'Commission des libertés civiles, de la justice et des affaires intérieures': u'LIBE',
               u'Committee on Environment, Public Health and Food Safety': u'ENVI',
               u'Committee on the Environment, Public Health and Food Safety': u'ENVI',
               u'Committee on Industry, Research and Energy': u'ITRE',
               u'Committee on Internal Market and Consumer Protection': u'IMCO',
               u'Committee on the Internal Market and Consumer Protection': u'IMCO',
               u'Committee on Transport and Tourism': u'TRAN',
               u'Committee on Regional Development': u'REGI',
               u'Committee on Agriculture and Rural Development': u'AGRI',
               u'Committee on Agricultural and Rural Development': u'AGRI',
               u'Committee on Committee on Agriculture and Rural Development': u'AGRI',
               u"Commission de l'agriculture et du développement rural": u'AGRI',
               u"Commission du marché intérieur et de la protection des consommateurs": u'IMCO',
               u'Co-Committee on the Internal Market and Consumer Protection': u'IMCO',
               u'COMMITTEE ON THE INTERNAL MARKET AND CONSUMER PROTECTION': u'IMCO',
               u'Committee on Fisheries': u'PECH',
               u'Committee on Culture and Education': u'CULT',
               u'Committee on Legal Affairs': u'JURI',
               u'Committee on Civil Liberties, Justice and Home Affairs': u'LIBE',
               u'Committee on Constitutional Affairs': u'AFCO',
               u"Committee on Women's Rights and Gender Equality": u'FEMM',
               u"Committee on Women’s Rights and Gender Equality": u'FEMM',
               u'Committee on Petitions': u'PETI',
               u'Committee on Financial, Economic and Social Crisis': u'CRIS',
               u'Committee on Policy Challenges Committee': u'SURE'}

STAGEMAP = {'Preparatory phase in Parliament': u'01. Preparatory phase in EP',
            'Awaiting Parliament 1st reading / single reading / budget 1st stage': u'02. EP 1st reading',
            'Awaiting Council 1st reading position / budgetary conciliation convocation': u'03. EC 1st reading position',
            'Awaiting reconsultation': u'04. Awaiting reconsultation',
            'Awaiting Parliament decision after Council rejection of joint text': u'05. EP decision after EC rejection of joint text',
            'Awaiting Council decision, blocked at 1st reading': u'06. EC decision, blocked at 1st reading',
            'Awaiting Parliament 2nd reading': u'07. EP 2nd reading',
            'Awaiting Council decision, 2nd reading': u'08. EC decision, 2nd reading',
            'Awaiting Parliament and Council decision, 3rd reading': u'09. EP and EC decision, 3rd reading',
            'Conciliation ongoing': u'10. Conciliation ongoing',
            'Political agreement on final act': u'11. Political agreement on final act',
            'Awaiting signature': u'12. Awaiting signature',
            'Awaiting final decision': u'13. Awaiting final decision',}

STAGES = ['Preparatory phase in Parliament',
          'Awaiting Parliament 1st reading / single reading / budget 1st stage',
          'Awaiting reconsultation',
          'Awaiting Council decision, blocked at 1st reading',
          'Awaiting Council 1st reading position / budgetary conciliation convocation',
          'Budgetary conciliation committee convened',
          'Awaiting announcement of budgetary joint text',
          'Awaiting budgetary conciliation report',
          'Awaiting Parliament decision on budgetary joint text',
          'Awaiting Council decision on budgetary joint text',
          'Awaiting Parliament decision after Council rejection of joint text',
          'Awaiting Parliament 2nd reading',
          'Awaiting Council decision, 2nd reading',
          'Conciliation ongoing',
          'Conciliation ended',
          'Awaiting Parliament and Council decision, 3rd reading',
          'Political agreement on final act',
          'Awaiting signature',
          'Awaiting final decision',
          'Procedure completed, awaiting publication in Official Journal']

ALL_STAGES= [ "Preparatory phase in Parliament",
              "Awaiting Parliament 1st reading / single reading / budget 1st stage",
              "Awaiting reconsultation",
              "Awaiting Council decision, blocked at 1st reading",
              "Awaiting Council 1st reading position / budgetary conciliation convocation",
              "Budgetary conciliation committee convened",
              "Awaiting announcement of budgetary joint text",
              "Awaiting budgetary conciliation report",
              "Awaiting Parliament decision on budgetary joint text",
              "Awaiting Council decision on budgetary joint text",
              "Awaiting Parliament decision after Council rejection of joint text",
              "Awaiting Parliament 2nd reading",
              "Awaiting Council decision, 2nd reading",
              "Conciliation ongoing",
              "Conciliation ended",
              "Awaiting Parliament and Council decision, 3rd reading",
              "Political agreement on final act",
              "Awaiting signature",
              "Awaiting final decision",
              "Procedure completed, awaiting publication in Official Journal",
              "Procedure completed",
              "Procedure rejected",
              "Procedure lapsed or withdrawn"]

buildings={ u"Altiero Spinelli": u'ASP',
            u"Willy Brandt": u'WIB',
            u"Paul-Henri Spaak": u'PHS',
            u"Atrium": u"ATR",
            u"Louise Weiss": u'LOW',
            u"Winston Churchill": u'WIC',
            u'Salvador de Madariaga': u"SDM",
            u"Bât. Altiero Spinelli": u'ASP',
            u"Bât. Willy Brandt": u'WIB',
            u"Bât. Paul-Henri Spaak": u'PHS',
            u"Bât. Atrium": u"ATR",
            u"Bât. Louise Weiss": u'LOW',
            u"Bât. Winston Churchill": u'WIC',
            u'B\xe2t. Salvador de Madariaga': u"SDM",
            }

ipexevents={u'CSL 1R Agreement': {'body': u'CSL', 'oeil': ['Council meeting'], },
            u'CSL Common Position': {'body': u'CSL', 'oeil': ['Council position'], },
            u'CSL Final Adoption': {'body': u'CSL',},
            u'CSL Final Agreement': {'body': u'CSL',},
            u'CSL Non Acceptance': {'body': u'CSL',},
            u'Date': {'body': u'EP', 'oeil': ['Initial legislative document', 'Commission/Council: initial legislative document', 'Legislative proposal published', 'Initial legislative proposal published', 'Modified legislative proposal published'], },
            u'Deadline Amendments': {'body': u'EP',},
            u'EP 1R Committee': {'body': u'EP', 'oeil': ['Vote scheduled in committee, 1st reading/single reading', 'EP: decision of the committee responsible, 1st reading/single reading'], },
            u'EP 1R Plenary': {'body': u'EP', 'oeil': ['EP: position, 1st reading or single reading'], },
            u'EP 2R Committee': {'body': u'EP', 'oeil': ['EP: decision of the committee responsible, 2nd reading'], },
            u'EP 2R Plenary': {'body': u'EP', 'oeil': ['EP: position, 2nd reading'], },
            u'EP 3R Plenary': {'body': u'EP', 'oeil': ['EP: legislative resolution, 3rd reading'], },
            u'EP Conciliation Committee': {'body': u'EP', 'oeil': ['Results of conciliation'], },
            u'EP officialisation': {'body': u'EP', 'oeil': ['Commission/Council: initial legislative document'], },
            u'End Date': {'body': u'EP', 'oeil': ['Final legislative act'], },
            u'Foreseen CSL Activities': {'body': u'CSL',},
            u'Prev Adopt in Cte': {'body': u'EP',},
            u'Prev DG PRES': {'body': u'EC', 'oeil' : ['Indicative plenary sitting date, 1st reading/single reading']},
            }

COUNTRIES = {'BE': u'Belgium',
             'BG': u'Bulgaria',
             'CZ': u'Czech Republic',
             'DK': u'Denmark',
             'DE': u'Germany',
             'EE': u'Estonia',
             'IE': u'Ireland',
             'EL': u'Greece',
             'ES': u'Spain',
             'FR': u'France',
             'IT': u'Italy',
             'CY': u'Cyprus',
             'LV': u'Latvia',
             'LT': u'Lithuania',
             'LU': u'Luxembourg',
             'HU': u'Hungary',
             'MT': u'Malta',
             'NL': u'Netherlands',
             'AT': u'Austria',
             'PL': u'Poland',
             'PT': u'Portugal',
             'RO': u'Romania',
             'SI': u'Slovenia',
             'SK': u'Slovakia',
             'FI': u'Finland',
             'SE': u'Sweden',
             'UK': u'United Kingdom',
             'GB': u'United Kingdom',
             'HR': u'Croatia',
             }

SEIRTNUOC = {'Belgium': u'BE',
             'Bulgaria': u'BG',
             'Czech Republic': u'CZ',
             'Denmark': u'DK',
             'Germany': u'DE',
             'Estonia': u'EE',
             'Ireland': u'IE',
             'Greece': u'EL',
             'Spain': u'ES',
             'France': u'FR',
             'Italy': u'IT',
             'Cyprus': u'CY',
             'Latvia': u'LV',
             'Lithuania': u'LT',
             'Luxembourg': u'LU',
             'Hungary': u'HU',
             'Malta': u'MT',
             'Netherlands': u'NL',
             'Austria': u'AT',
             'Poland': u'PL',
             'Portugal': u'PT',
             'Romania': u'RO',
             'Slovenia': u'SI',
             'Slovakia': u'SK',
             'Finland': u'FI',
             'Sweden': u'SE',
             'United Kingdom': u'GB',
             }

GROUPS=[
   'Communist and Allies Group',
   'European Conservative Group',
   'European Conservatives and Reformists',
   'European Democratic Group',
   'Europe of freedom and democracy Group',
   'Europe of Nations Group (Coordination Group)',
   'Forza Europa Group',
   'Confederal Group of the European United Left',
   'Confederal Group of the European United Left/Nordic Green Left',
   'Confederal Group of the European United Left - Nordic Green Left',
   'Christian-Democratic Group',
   "Christian-Democratic Group (Group of the European People's Party)",
   "Group of the European People's Party ",
   'Group for a Europe of Democracies and Diversities',
   'Group for the European United Left',
   'Group for the Technical Coordination and Defence of Indipendent Groups and Members',
   'Group of Independents for a Europe of Nations',
   'Group of the Alliance of Liberals and Democrats for Europe',
   'Group of the European Democratic Alliance',
   'Group of the European Liberal, Democrat and Reform Party',
   'Group of the European Radical Alliance',
   'Group of the European Right',
   'Group of the Greens/European Free Alliance',
   'Group of the Party of European Socialists',
   'Group of the Progressive Alliance of Socialists and Democrats in the European Parliament',
   'European Democratic Union Group',
   'Group of European Progressive Democrats',
   "Group of the European People's Party (Christian Democrats) and European Democrats",
   "Group of the European People's Party (Christian Democrats)",
   'Group Union for Europe',
   'Identity, Tradition and Sovereignty Group',
   'Independence/Democracy Group',
   'Left Unity',
   'Liberal and Democratic Group',
   'Liberal and Democratic Reformist Group',
   'Non-attached',
   'Non-attached Members',
   "Rainbow Group: Federation of the Green Alternative European Links, Agelev-Ecolo, the Danish People's Movement against Membership of the European Community and the European Free Alliance in the European Parliament",
   'Rainbow Group in the European Parliament',
   'Socialist Group',
   'Socialist Group in the European Parliament',
   'Technical Coordination and Defence of Independent Groups and Members',
   'Technical Group of Independent Members - mixed group',
   'Technical Group of the European Right',
   'The Green Group in the European Parliament',
   'Union for Europe of the Nations Group', ]

group_map={ u"Confederal Group of the European United Left - Nordic Green Left": u'GUE/NGL',
            u"Confederal Group of the European United Left-Nordic Green Left": u'GUE/NGL',
            u'Confederal Group of the European United Left / Nordic Green Left': u'GUE/NGL',
            u'Confederal Group of the European United Left/Nordic Green Left': u'GUE/NGL',
            u'Confederal Group of the European United Left': u'GUE/NGL',
            u"European Conservatives and Reformists": u'ECR',
            u'European Conservatives and Reformists Group': u'ECR',
            u"Europe of freedom and democracy Group": u'EFD',
            u'Europe of Freedom and Democracy Group': u'EFD',
            u"Group of the Alliance of Liberals and Democrats for Europe": u'ALDE',
            u'Liberal and Democratic Reformist Group': u'LDR',
            u'Group Union for Europe': u'UFE',
            u'European Democratic Group': u'EDG',
            u'Liberal and Democratic Group': u'ALDE',
            u'Technical Group of the European Right': u'DR',
            u'Group of the European Radical Alliance': u'ERA',
            u'Group of the European Democratic Alliance': u'EDA',
            u"Group of the Greens/European Free Alliance": u"Verts/ALE",
            u"Group of the Progressive Alliance of Socialists and Democrats in the European Parliament": u"S&D",
            u'Group for a Europe of Democracies and Diversities': u'EDD',
            u'Group of the European Liberal Democrat and Reform Party': u'ELDR',
            u'Group of the European Liberal, Democrat and Reform Party': u'ELDR',
            u'Group indépendence/Démocratie': [u'ID',u'INDDEM', u'IND/DEM'],
            u'Independence/Democracy Group': [u'ID', u'INDDEM', u'IND/DEM'],
            u'Non-attached Members': [u'NA',u'NI'],
            u'Non-attached': [u'NA',u'NI'],
            u'Identity, Tradition and Sovereignty Group': u'ITS',
            u"Group of the European People's Party (Christian Democrats) and European Democrats": u'PPE-DE',
            u"Group of the European People's Party (Christian Democrats)": u'PPE',
            u"Group of the European People's Party (Christian-Democratic Group)": u"PPE",
            u'Group of the Party of European Socialists': u'PSE',
            u'Socialist Group in the European Parliament': u'PSE',
            u'Technical Group of Independent Members': u'TDI',
            u'Group indépendence/Démocratie': u'UEN',
            u'Union for a Europe of Nations Group': u'UEN',
            u'Union for Europe of the Nations Group': u'UEN',
            u'Group of the Greens / European Free Alliance': u'Verts/ALE',
            u'The Green Group in the European Parliament': u'Verts/ALE',
            u'Greens/EFA': u'Verts/ALE',
            }
groupids=[]
for item in group_map.values():
    if type(item)==list:
        groupids.extend(item)
    else:
        groupids.append(item)

CELEXCODES={
    "1": { "Sector": u"Treaties",
           "Document Types" : { "D": u"Treaty of Amsterdam 1997",
                                "M": u"Treaty on the European Union, Maastricht 1992 - EU Treaty - consolidated version 1997",
                                "E": u"EEC Treaty 1957 - EEC Treaty - consolidated version 1992 - EEC Treaty - consolidated version 1997",
                                "K": u"ECSC Treaty 1951",
                                "A": u"EURATOM Treaty 1957",
                                "U": u"Single European Act 1986",
                                "G": u"Groenland Treaty 1985",
                                "R": u"Treaty amending certain financial provisions 1975",
                                "F": u"Treaty amending certain budgetary provisions 1970",
                                "F": u"Merger Treaty 1965",
                                "B": u"Accession Treaty 1972 (United Kingdom, Denmark, Ireland, Norway)",
                                "H": u"Accession Treaty 1979 (Greece)",
                                "I": u"Accession Treaty 1985 (Spain, Portugal)",
                                "N": u"Accession Treaty 1994 (Austria, Sweden, Finland, Norway)",
                                "T": u"Accession Treaty 2003 (Slovakia, Estonia, Poland, Hungary, Lithuania, Latvia, Slovenia, Cyprus, Czech Republic, Malta)",
                                }},
    "2": { "Sector": u"External Agreements",
           "Document Types" : { "A":u"Agreements with non-member States or international organisations",
                                "D":u"Acts of bodies created by international agreements",
                                "P":u"Acts of parliamentary bodies created by international agreements",
                                "X":u"Other Acts ",},},
    "3": { "Sector": u"Legislation",
           "Document Types" : { "E":u"Common Foreign and Security Policy (CFSP) - common positions / joint actions / common strategies",
                                "F":u"Justice and Home Affairs (JHA) - common positions / framework decisions",
                                "R":u"Regulations",
                                "L":u"Directives",
                                "D":u"Decisions sui generis",
                                "S":u"ECSC Decisions of general interest",
                                "M":u"Non-opposition to a notified concentration",
                                "J":u"Non-opposition to a notified joint venture",
                                "B":u"Budget",
                                "K":u"Recommendations ECSC",
                                "O":u"Guidelines ECB",
                                "H":u"Recommendations",
                                "A":u"Avis",
                                "G":u"Resolutions",
                                "C":u"Declarations",
                                "Q":u"Institutional arrangements, Rules of Procedure, Internal agreements",
                                "X":u"Other documents",},},
    "4": { "Sector": u"Internal Agreements",
           "Document Types" : { "D":u"Decisions of the representatives of the governments of the Member States",
                                "X":u"Other acts",},},
    "5": { "Sector": u"Proposals + preparatory documents",
           "Document Types" : { "AG":u"Council - common positions",
                                "KG":u"Council - assent ECSC",
                                "IG":u"Member States - Initiatives",
                                "XG":u"Council - other acts",
                                "PC":u"COM Documents - proposals for legislation",
                                "DC":u"COM Documents - other documents",
                                "SC":u"SEC Documents",
                                "XC":u"Commission - other acts",
                                "AP":u"EP - legislative resolution",
                                "BP":u"EP - budget",
                                "IP":u"EP - other resolutions",
                                "XP":u"EP - other acts",
                                "AA":u"Court of Auditors - opinions",
                                "TA":u"Court of Auditors - reports",
                                "SA":u"Court of Auditors - special reports",
                                "XA":u"Court of Auditors - other acts",
                                "AB":u"ECB - opinions",
                                "HB":u"ECB - recommendations",
                                "XB":u"ECB - other acts",
                                "AE":u"ESC - opinions on consultation",
                                "IE":u"ESC - other opinions",
                                "XE":u"ESC - other acts",
                                "AR":u"CR - opinions on consultation",
                                "IR":u"CR - other opinions",
                                "XR":u"CR - other acts",
                                "AK":u"ECSC Com. - opinions",
                                "XK":u"ECSC Com. - other acts",
                                "XX":u"Other acts ", }, },
    "6": { "Sector": u"Case Law",
           "Document Types" : { "A":u"Court of First Instance Judgments",
                                "B":u"Court of First Instance - Orders",
                                "D":u"Court of First Instance - Third Party Proceedings",
                                "F":u"Court of First Instance - Opinions",
                                "H":u"Court of First Instance - Case report",
                                "C":u"Court of Justice - Conclusions of the Avocate-General",
                                "J":u"Court of Justice - Judgments",
                                "O":u"Court of Justice - Orders",
                                "P":u"Court of Justice - Case report",
                                "S":u"Court of Justice - Seizure",
                                "T":u"Court of Justice - Third Party Proceedings",
                                "V":u"Court of Justice - Opinions",
                                "X":u"Court of Justice - Rulings",},},
    "7": { "Sector": u"National Implementation",
           "Document Types" : {"L":u"National Implementation Measures - implementation of directives",},},
    "9": { "Sector": u"European Parliamentary Questions",
           "Document Types" : { "E":u"European European Parliament - Written Questions",
                                "H":u"European European Parliament - Questions at Questiontime",
                                "O":u"European European Parliament - Oral questions",},},
    "C": { "Sector": u"OJC Documents", "Document Types" : {},},
    "E": { "Sector": u"EFTA Documents",
           "Document Types" : { "A":u"International Agreements",
                                "C":u"Acts of the EFTA Surveillance Authority",
                                "G":u"Acts of the EFTA Standing Committee",
                                "J":u"Decisions, Orders, Consultative opinions of the EFTA Court",
                                "P":u"Pending cases of the EFTA Court",
                                "X":u"EFTA - Other Acts",},},
    }
