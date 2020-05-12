Yu Group Website Maintenance Manual

1. Publications
	- Install bibtex2html: http://www.lri.fr/~filliatr/bibtex2html/.  To install bibtex2html on ubuntu, you only need command "apt-get install bibtex2html".
	- Go to folder "maintenance/publications" and replace the existing "yugroup.bib" with the latest version.
	- Execute "sh script.sh".
	- Copy the newly generated "index.html" to folder "publication" and replace the current "index.html" file.


2. People
	- Add the new person's photo to folder "fig"
	- Go to folder "people" and open "index.html" with TextMate or any .css editor.
	- The general format of a student profile: (contents in ** need to be replaced by actual contents)
	    <tr>
	    	<td>&nbsp;</td>
	    	<td><img src="../fig/*new_student_photo.png*" width="100" /></td>
	    	<td class="Names"><a href="*new_student_webpage_address*" target="_new">*new_student_name*</a></td>
	    	<td class="Names">&nbsp;</td>
	    	<td class="DescriptionPpl">*new_student_description*</td>
	    	<td>&nbsp;</td>
	    </tr>


3. Contact+Photos
	- Add the new photo to folder "fig"
	- Duplicate the photo and name the extra copy "current.jpg" (replace the existing current.jpg).
	- Go to folder "contact" and open "index.html" to add a new entry on the website
	- The general format of a new group photo:
		<tr>
			<td>&nbsp;</td>
			<td class="DescriptionRight">*yyyy/mm/dd*</td>
			<td>&nbsp;</td>
			<td colspan="7"><a name="f*2011*" id="f*2011*"></a><img src="../fig/*yugroup_new_photo.jpg*" width="95%"/></td>
			<td>&nbsp;</td>
		</tr>
		<tr>
  			<td>&nbsp;</td>
  			<td>&nbsp;</td>
  			<td>&nbsp;</td>
  			<td colspan="7" class="DescriptionRes">*List of people in the photo.*</td>
  			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td colspan="7">&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
	- In index.html search for "<td colspan="2" class="DescriptionRight">PHOTOS</td>" to locate the bookmark definitions at the top of the page.  Add bookmark for the new photo:
 		<td width="10%" class="DescriptionRight"><a href="#f*yyyy*">*yyyy*</a></td>
		

4. Research and Memo pages can be updated in a similar way.


 -- 2012 FEB