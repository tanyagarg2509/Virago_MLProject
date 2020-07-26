The data represented 50 ids from Formspring.me that were crawled in Summer 2010.

For each id, the profile information and each post (question and answer) was extracted.

Each post was loaded into Amazon's mechanical turk and labeled by three workers for cyberbullying content.

The data contains the following profile fields:
BIO - profile biography created by owner of the id
DATE - the date the id was crawled
LOCATION - location provided by the owner of the id
USERID - The actual id itself

The data contains the following information on each post
TEXT - the question and answer (separated by a
)
ASKER - the id of the person asking the question (blank if anonymous)

3 occurrences of LABELDATA:
    ANSWER - YES or NO as to whether the post contains cyberbullying
    CYBERBULLYINGWORK - word(s) or phrase(s) identified by the mechanical turk worker as the reason it was tagged as cyberbullying (n/a or blank if no cyberbullying detected)
    SEVERITY - cyberbullying severity from 0 (no bullying) to 10 
    OTHER - other comments from the mechanical turk worker
    WORKTIME - time needed to label the post (in seconds)
    WORKER - mechanical turk worker id
Information on how this data was used is available at:

Reynolds, K, A. Kontostathis and L. Edwards. 2011. Using Machine Learning to Detect Cyberbullying. In Proceedings of the 2011 10th International Conference on Machine Learning and Applications Workshops (ICMLA 2011). December 2011. Honolulu, HI.

This material is based upon work supported by the National Science Foundation under Grant No. 0916152.   Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

I am currently working on detecting cyberbullying among teenagers in social media. In both physical and cyber worlds, Bullying has been recognized as a serious national health issue among adolescents. . The potential of sentiment analysis can help identify victims who pose high risk to themselves or others, and to enhance the scientific understanding of bullyiing overall.