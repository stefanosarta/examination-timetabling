## Σύντομη περιγραφή

Το συγκεκριμένο πρόβλημα έχει να κάνει με τον χρονοπρογραμματισμό μιας εξεταστικής διαδικασίας για παράδειγμα, ενός Πανεπιστημίου. Αφορά την ορθή τοποθέτηση των περιόδων έτσι ώστε λόγω της εξέτασης που πραγματοποιείται σε κάθε μία από αυτές να μην προκύψει σύγκρουση λόγω εγγραφής κάποιου σπουδαστή. Δηλαδή, να μην υπάρχει κάποιος δπουδαστής που θα απαιτηθεί να συμμετάσχει σε περισσότερα του ενός μαθήματος στην ίδια περίοδο.

Η εφαρμογή που φτιάχτηκε είναι σε θέση να λύσει το πρόβλημα αυτό και να επιστρέψει ως αποτέλεσμα εκτός από ένα αρχείο με κατάληξη .sol που περιέχει μέσα την κάθε εξέταση και την περίοδο που τοποθετείται αλλά και το κόστος της επίλυσης. Το κόστος της επίλυσης προκύπτει από τις περιόδους που θα τοποθετηθεί ο κάθε φοιτητής ώστε να δώσει το μάθημα. Εκτός προφανώς της απαγόρευσης να συμμετάσχει στην ίδια περίοδο έχοντας σε αυτή την περίπτωση αποτυχία επίλυσης, έχουν οριστεί ποινές των 16,8,4,2,1 για εξετάσεις που απέχουν 1,2,3,4 ή 5 περιόδους αντίστοιχα. Το τελικό αποτέλεσμα αφορά την συνολική ποινή που προστίθεται για κάθε φοιτητή με την διαίρεση του συνολικού αριθμού των φοιτητών.

## Οδηγίες εγκατάστασης
Η επίλυση του προβλήματος πραγματοποιήθηκε με την γλώσσα προγραμματισμού Python και συγκεκριμένα την έκδοση
```markdown
$ python3 --version
Python 3.8.5
```



$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 20.04.1 LTS
Release:	20.04
Codename:	focal


$ python3 --version
Python 3.8.5




You can use the [editor on GitHub](https://github.com/stefanosarta/examination-timetabling/edit/main/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/stefanosarta/examination-timetabling/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
