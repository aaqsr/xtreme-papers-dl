# xtremepaper downloader

**NOTE: AS OF NOW, ON WINDOWS THE FOLDER PATH WILL NOT WORK, PLEASE EDIT THE `folder_path` VARIABLE IN XTREME.py**

## CHANGELOG

Old repo hadn't been updated for a few years. As such it was not working. 
So I thought I'd fork it and fix it.
As of now on my mac the download for papers works for O LEVEL papers. 
Just be sure to add your own urls. (The get code system has not been tested but is left in for now until it can be verified to be working.)

The first important priority for me was getting the core parts of this up and running.
I don't have time as of now, but the second I do, I'll probably make many more changes and fixes.

Original repo by CubeOvO. Mirrored with permission :)

## OLD README

my current python version : 3.5.2


*now is quicker than ever before - multiprocessing implimented. download all the papers in a few minitues.*


*won't work in py2*

### required module:
* BeautifulSoup
* requests
* urllib
* lxml

Do ```pip install -r example-requirements.txt```
Note: If you get an error concerning the lxml parser, uninstall then reinstall lxml via pip.
  
### input:
* input syllabus code (recommend) - currently support ~~following~~ all syllabus code
* local syllabus code - local stored syllabus code are as follows

```
	'5070':'https://papers.xtremepape.rs/CAIE/O%20Level/Chemistry%20(5070)/',
    	'5040':'https://papers.xtremepape.rs/CAIE/O%20Level/Physics%20(5054)/'
```
More can easily be added in XTREME.py by adding them to `url_list`

* *new feature* - get other syllabus code online
* input url - please input similar url at above, where the links in the webpages links directly to pdfs you want to download but not the subject(s) o.w. this programe won't work (although it'll acts like it worked)

### Example input 1 - input local syllabus code:

	please provide the syllabus number of the papers you wants to download:9701
	detected syllabus code, processing...
	Now starts to download, this may (defintely) take some times so you may want to
	go and grab yourself some drink and let this programe run alone.
	file already exists 9701_33_5RP_AFP_TSS.pdf
	file already exists 9701_33_CI_4RP_AFP_TSS.pdf
	file already exists 9701_Chemistry_Data_Booklet_2016.pdf
	detected new file. successfully downloaded 9701_Chemistry_Data_Booklet_specimen_
	2016.pdf
	detected new file. successfully downloaded 9701_Chemistry_Example_Candidate_Resp
	detected new file. successfully downloaded 9701_nos_as_4.pdf
	detected new file. successfully downloaded 9701_nos_as_5.pdf
    ...


### Example input 2 - input url directly:
    please provide the syllabus number of the papers you wants to download:http://pa
    pers.xtremepapers.com/CIE/Cambridge%20International%20A%20and%20AS%20Level/Japan
    ese%20Language%20%28AS%20Level%20only%29%20%288281%29/
    syllabus code did not detected
    downloading form the website http://papers.xtremepapers.com/CIE/Cambridge%20Inte
    rnational%20A%20and%20AS%20Level/Japanese%20Language%20%28AS%20Level%20only%29%2
    0%288281%29/
    Now starts to download, this may (defintely) take some times so you may want to
    go and grab yourself some drink and let this programe run alone.
    file already exists 8281_w05_er.pdf
    file already exists 8281_w05_qp_2.pdf
    ...
    file already exists 8281_y16_sy.pdf
    successfully downloaded all the files available at http://papers.xtremepapers.co
    m/CIE/Cambridge%20International%20A%20and%20AS%20Level/Japanese%20Language%20%28
    AS%20Level%20only%29%20%288281%29/

### *Example input 3 - search syllabus code online
	please provide the syllabus number of the papers you wants to download:9011
	syllabus code did not match local database, do you wish to get online database f
	or syllabus code?
	y
	Searching at online data base at https://papers.xtremepapers.com/CIE/Cambridge I
	nternational A and AS Level/
	detected syllabus code, processing...
	Now starts to download, this may (defintely) take some times so you may want to
	go and grab yourself some drink and let this programe run alone.
	creating new folder .\Divinity%20%289011%20and%208041%29\
	detected new file. successfully downloaded 8041_9011_Example_Candidate_Responses
	_Booklet_2011_WEB.pdf
	detected new file. successfully downloaded 8041_w03_er.pdf
	detected new file. successfully downloaded 8041_w03_qp_2.pdf
	detected new file. successfully downloaded 8041_w04_er.pdf
	detected new file. successfully downloaded 8041_w04_qp_2.pdf
	detected new file. successfully downloaded 8041_w05_er.pdf
