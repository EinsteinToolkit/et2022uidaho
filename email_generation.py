from collections import namedtuple

invited_speakers_tuple = namedtuple("invited_speakers_tuple","firstName lastName talkType talkTopic talkDate talkTime talkDuration talkOrder email")

invited_speakers_dict = {}

# Plenary speakers
invited_speakers_dict["Example"] = invited_speakers_tuple("FirstName","LastName","plenary talk","Example plenary talk","Monday, June 13, 2022","08:25 AM","40min", "01","example@example.com")


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
