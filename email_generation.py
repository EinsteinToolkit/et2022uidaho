from collections import namedtuple

invited_speakers_tuple = namedtuple("invited_speakers_tuple","firstName lastName talkType talkTopic talkDate talkTime talkDuration talkOrder email")

invited_speakers_dict = {}

# Plenary speakers
invited_speakers_dict["Campaneli"   ] = invited_speakers_tuple("Manuela" ,"Campaneli"   ,"plenary talk","An overview of numerical relativity"           ,  "Monday, June 13, 2022","08:25 AM",  "40min", "01","manuela@astro.rit.edu")
invited_speakers_dict["Okounkova"   ] = invited_speakers_tuple("Masha"   ,"Okounkova"   ,"plenary talk","Numerical relativity beyond general relativity",  "Monday, June 13, 2022","09:05 AM",  "40min", "02","mokounkova@flatironinstitute.org")
invited_speakers_dict["Duez"        ] = invited_speakers_tuple("Matt"    ,"Duez"        ,"lecture"     ,"Introduction to General Relativistic MHD"      ,  "Monday, June 13, 2022","11:25 AM",  "40min", "03","m.duez@wsu.edu")
invited_speakers_dict["Zlochower"   ] = invited_speakers_tuple("Yosef"   ,"Zlochower"   ,"tutorial"    ,"Writing an Einstein Toolkit thorn"             ,  "Monday, June 13, 2022","03:40 PM","1h45min", "04","yosef@astro.rit.edu")
invited_speakers_dict["Tichy"       ] = invited_speakers_tuple("Wolfgang","Tichy"       ,"talk"        ,"The SGRID initial data code"                   , "Tuesday, June 14, 2022","08:25 AM",  "40min", "05","wolf@fau.edu")
invited_speakers_dict["Grandclément"] = invited_speakers_tuple("Philippe","Grandclément","talk"        ,"The Kadath initial data code"                  , "Tuesday, June 14, 2022","09:10 AM",  "40min", "06","philippe.grandclement@obspm.fr")
invited_speakers_dict["Assumpção"   ] = invited_speakers_tuple("Thiago"  ,"Assumpção"   ,"lecture"     ,"The NRPyElliptic initial data code"            , "Tuesday, June 14, 2022","10:25 AM",  "40min", "07","assumpcaothiago@gmail.com")
invited_speakers_dict["Vu"          ] = invited_speakers_tuple("Nils"    ,"Vu"          ,"lecture"     ,"The SpeCTRE initial data solver"               , "Tuesday, June 14, 2022","11:10 AM",  "40min", "08","nils.vu@black-holes.org")
invited_speakers_dict["Gupte"       ] = invited_speakers_tuple("Tanmayee","Gupte"       ,"tutorial"    ,"Generating neutron star ID with LORENE"        , "Tuesday, June 14, 2022","01:25 PM","1h45min", "09","tmg9722@rit.edu")
invited_speakers_dict["Crosas"      ] = invited_speakers_tuple("Mercè"   ,"Crosas"      ,"talk"        ,"Data formats for numerical relativity"         ,"Thursday, June 16, 2022","08:25 AM",  "40min", "10","mcrosas@g.harvard.edu")
invited_speakers_dict["Clough"      ] = invited_speakers_tuple("Katy"    ,"Clough"      ,"talk"        ,"GRChombo"                                      ,"Thursday, June 16, 2022","09:10 AM",  "40min", "11","katy.a.clough@gmail.com")
invited_speakers_dict["Stein"       ] = invited_speakers_tuple("Leo"     ,"Stein"       ,"talk"        ,"Black Hole Perturbation Toolkit"               ,"Thursday, June 16, 2022","10:25 AM",  "40min", "12","lcstein@olemiss.edu")
invited_speakers_dict["Schmidt"     ] = invited_speakers_tuple("Patricia","Schmidt"     ,"lecture"     ,"Gravitational wave modeling"                   ,"Thursday, June 16, 2022","11:10 AM",  "40min", "13","pschmidt@star.sr.bham.ac.uk")
invited_speakers_dict["Warburton"   ] = invited_speakers_tuple("Niels"   ,"Warburton"   ,"tutorial"    ,"The black hole perturbation toolkit"           ,"Thursday, June 16, 2022","01:25 PM","1h45min", "14","niels.warburton@ucd.ie")
invited_speakers_dict["Bozzola"     ] = invited_speakers_tuple("Gabriele","Bozzola"     ,"tutorial"    ,"Visualizing data with Kuibit"                  ,"Thursday, June 16, 2022","03:40 PM","1h45min", "15","gabrielebozzola@email.arizona.edu")
invited_speakers_dict["Schnetter"   ] = invited_speakers_tuple("Erik"    ,"Schnetter"   ,"talk"        ,"Future of the Einstein Toolkit: CarpetX"       ,  "Friday, June 17, 2022","08:25 AM",  "40min", "16","eschnetter@perimeterinstitute.ca")
invited_speakers_dict["Giacomazzo"  ] = invited_speakers_tuple("Bruno"   ,"Giacomazzo"  ,"talk"        ,"The Spritz code"                               ,  "Friday, June 17, 2022","09:10 AM",  "40min", "17","bruno.giacomazzo@unimib.it")
invited_speakers_dict["Lovelace"    ] = invited_speakers_tuple("Geoffrey","Lovelace"    ,"talk"        ,"The SpEC and SPECTRE codes"                    ,  "Friday, June 17, 2022","09:10 AM",  "40min", "18","glovelace@fullerton.edu")
invited_speakers_dict["Kalinani"    ] = invited_speakers_tuple("Jay"     ,"Kalinani"    ,"tutorial"    ,"Writing GPU codes for the Einstein Toolkit"    ,  "Friday, June 17, 2022","01:25 PM","1h45min", "19","jayvijay.kalinani@phd.unipd.it")
invited_speakers_dict["Cupp"        ] = invited_speakers_tuple("Sam"     ,"Cupp"        ,"tutorial"    ,"EMRIs with the Einstein Toolkit"               ,  "Friday, June 17, 2022","03:40 PM","1h45min", "20","scupp1@my.apsu.edu")

# for speaker_key in invited_speakers_dict:
#     speaker = invited_speakers_dict[speaker_key]
#     print(f"{speaker.firstName} {speaker.lastName} will be invited to give a {speaker.talkType} on {speaker.talkDate} at {speaker.talkTime} on \"{speaker.talkTopic}\".")


def compose_email(speaker):
    emailBody = f"""

From: leonardo@uidaho.edu
To: {speaker.email}
CC:
Gabrielle Allen <gdallen@uwyo.edu>,
Steven Brandt <sbrandt@cct.lsu.edu>,
Zachariah Etienne <zetienne@uidaho.edu>,
Roland Haas <rhaas@illinois.edu>,
Christiana Pantelidou <christiana.pantelidou@ucd.ie>,
Helvi Witek <hwitek@illinois.edu>,
workshop@einsteintoolkit.org

Dear {speaker.firstName},

We would like to invite you to participate in the 2022 North American Einstein
Toolkit Workshop/Summer School and give a {speaker.talkType} on the topic of
“{speaker.talkTopic}.”

The Workshop will take place June 13-17, 2022, at the University of Idaho in
Moscow, Idaho. We anticipate your talk will take place on {speaker.talkDate} at
{speaker.talkTime} US Pacific Time, though please let us know if another time/date would
work better for you.

The Workshop/School will be in a hybrid format, and you are more than welcome to
both give your {speaker.talkType} and attend either in person or virtually (over
Zoom). Generally the {speaker.talkType} will be roughly {speaker.talkDuration} in duration"""
    if speaker.talkType != "tutorial":
        emailBody += ", with 5 minutes for questions"
    emailBody += """.\nFinal details about timing will be provided in early May once the schedule is
finalized. Full details can be found on our website:
https://einsteintoolkit.github.io/et2022uidaho/

As a participant of the Workshop, financial support may be available to
partially cover your travel costs. Please let us know if you would be interested
in this support. Note that priority will be given to participants who will
attend the full week.

Please let us know if you would be willing to accept this invitation. We would
appreciate it if you could respond with your availability by March 31, 2022.

Thanks in advance for your consideration, and have a wonderful day.

Sincerely,

The Scientific Organizing Committee of the
2022 North American Einstein Toolkit Workshop/Summer School
Gabrielle Allen
Steven Brandt
Zachariah Etienne
Roland Haas
Christiana Pantelidou
Leonardo Werneck
Helvi Witek
"""
    return emailBody

for speaker_key in invited_speakers_dict:
    speaker = invited_speakers_dict[speaker_key]
    outfile = speaker.talkOrder+"-"+speaker.firstName+"_invitation_email.txt"
    with open(outfile,"w") as email:
        email.write(compose_email(speaker))
        print(f"Wrote email for {speaker.firstName} {speaker.lastName} to file \"{outfile}\"")
