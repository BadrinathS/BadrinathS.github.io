# Personal Website 

I am using website template from [m-niemeyer](https://m-niemeyer.github.io/). 



## How to use it
1. Update and adjust the name and bio text in the function `get_personal_data` in the `build.py` file.
2. Upload your own profile photo to `assets/img/profile.jpg`.
3. Replace `publications_list.pub` with your publications. Note that the entries are crawled from top to bottom, i.e. the first entries are shown at the top. Further, the entries contain additional fields like `html`, `code`, and more, that are used to generate the links to the project page, code, etc. Check out the function `get_paper_entry` in `build.py` for more information.
4. Replace `talk_list.pub` with your talks similar to before. Check out the function `get_talk_entry` in `build.py` for more information on accepted talk fields.
5. Update the author websites in the function `get_author_dict` in `builds.py` to automatically generate the links to your co-authors' websites.
6. Run `python build.py` which automatically generates the `index.html` file - the only file you need!
7. Add credits and a link to website.
 
