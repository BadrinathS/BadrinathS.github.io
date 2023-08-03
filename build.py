from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Badrinath", "Singhal"]
    email = "badrinath2602@gmail.com"
    twitter = "mrbadrinath"
    github = "BadrinathS"
    linkedin = "badrinath-s"
    bio_text = f"""

                <p>Hi, Thanks for dropping on this site, below are some academic/professional details about me. 
                Outside of professional life, I just try not to take things seriously. I enjoy cricket, running, comedy, food, tea, sunrise/sunset, mathematics etc.
                
                </p>
                <!-- <p>
                    <span style="font-weight: bold;">Research:</span>
                </p> -->
                <p>
                    <span style="font-weight: bold;">Bio:</span> 
                    Previously I worked at <a href="https://www.axera-tech.com/" target="_blank"> Axera Tech</a> and at <a href="https://embodyme.com/" target="_blank"> EmbodyMe </a> as a Machine Learning Scientist. And even before that I worked at <a href="https://synapsica.com/" target="_blank"> Synapsica </a>.  
                <br>
                <br>
                    I graduated from <a href="https://iitg.ac.in" target="_blank"> Indian Institute of Tehnology Guwahati </a> majoring in  Electronics and Electrical Engineering with minor in Computer Science and Engineering. 
                    For my secondary and senior secondary education I attended <a href="https://amerigogcrpf.kvs.ac.in/" target="_blank"> Kendriya Vidyalaya C.R.P.F. Amerigog </a>.
                    
                    <!-- During my junior year, I worked at <a href="http://fuzzy.hanyang.ac.kr/" target="_blank"> Computer Vision and Fuzzy Systems Lab</a> in <a href="https://www.hanyang.ac.kr/web/eng" target="_blank">Hanyang University </a> under the supervision of Prof. Frank Chung Hoon Rhee where I have worked in the field of Fuzzy logic with focus on "Interval Type 2 Fuzzy C Means Clustering algorithm". 
                    For my sophomore year, I worked at<a href="http://sacral.c.u-tokyo.ac.jp/" target="_blank"> Ikegami Lab </a> in <a href="https://www.u-tokyo.ac.jp/en/" target="_blank"> The University of Tokyo</a>. -->

                </p>
                <p>
                    Here is a <a href="https://www.youtube.com/watch?v=a1zDuOPkMSw&ab_channel=securitylectures">talk</a> from Richard Hamming about how to do great research, the talk is very practical and can be applied by any researcher across any field. 
                    It can be interpolated to any aspect of life and not necessarily in research. Although I find the <a href="https://www.cs.virginia.edu/~robins/YouAndYourResearch.html">transcript</a> of the talk more impactful than the video. Do listen to the lecture if you can. 

                </p>
                <p>
                Here is the <a href="https://www.youtube.com/watch?v=4SQfsBsMFls&ab_channel=ItamarSegal">video</a> of Neil Patric Harris hosting the Tony Awards 2013, I love to watch this video every once in a while. Every time I watch this, it puts a smile on my face and I hope it does the same to you. 
                </p>
                <p>Feel free to contact me if you want to discuss something or meet over coffee! I am also open to collaborations and feedback.</p>
                <p>
                    <a href="https://badrinaths.github.io/assets/pdf/Resume.pdf" target="_blank" style="margin-right: 15px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:badrinath2602@gmail.com" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/mrbadrinath" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> Twitter</a>
                    <a href="https://github.com/BadrinathS" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/badrinath-s/" target="_blank" style="margin-right: 15px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                    Credits for the website <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">in this link</a>.
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        # 'Yuanzhen Li': 'http://people.csail.mit.edu/yzli/',
        # 'Varun Jampani': 'https://varunjampani.github.io/'
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='None', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="margin-bottom: 1em;">
            <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
            </div>
            <br>
            <div class="col-md-8" style="">
                {bio_text}
            </div>
            <div class="col-md-4" style="">

                <img src="assets/img/profile.JPG" class="img-thumbnail" width="280px" alt="Profile picture">

            </div>
        </div>
        <div class="row" style="margin-top: 1em;">
            <div class="col-sm-12" style="">
                <h4>Publications</h4>
                {pub}
            </div>
        </div>
        <div class="row" style="margin-top: 3em;">
            <div class="col-sm-12" style="">
                <h4>Talks</h4>
                {talks}
            </div>
        </div>
        <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
            {footer}
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')