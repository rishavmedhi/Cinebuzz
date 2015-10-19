disc = ["a","an","the","of","is","was","in","during","got","are","did","took","belongs","to","has","at","on","and"
        ,"or","me","around","celebrated","celebrate","regarding","into","came","existence","exist","rule","legal","become"
	,"became","does","political","records","any","located","total","how","much","with","my","based","as","being"
	,"done","found","under","can","you","get","for","offered","offer","by","many","that","have","draw","it","so","draws"
	,"whome","included","include","through","go","said","happened","whom","whose","who","this","water","body","neft","having"
	,"what","overall","moving","travelling","travel","go","going","goes","moves"
	,"if","then","than","be","could","been","weapon","belong"
        ,"shown","hit","come","happen","strike","earthquake","related","relate","relates","relating","called","tell","known"
	, "famous","famously","prize","most","read","both","record","recorded","live","will","goes","stretch","run","over",
	  "pass","through","number","numbers","where","from","performed","won","olympics","university","talks","were"]
t = ["train","trains","passenger","express"]
w = ["weather","weathers","climate","climates","climatic"]
s = ["stock"]#other stock terms if required
m = ["gold","silver","oil"]#other mineral terms if required
sp = ["score","cricket"]#other sports terms if required
r = ["movie","director","cast","writer","producer","story","release","genre","rating","music","cinematographer","editor","review"]
e = ["exam","examination","exams","examinations","test","tests"]
loc = ["near","around","closest","nearest"]
mov = ["movie","director","cast","writer","producer","story","release","genre","rating","music","cinematographer","editor","review"]
low = ["less","lesser","lower","smaller"]
high = ["high","higher","more","greater"]
maxi = ["maximum","highest","tallest","largest","longest"]
mini = ["minimum","least","smallest","tiniest","deepest"]
avg = ["average","mean"]
summ = ["total","sum","aggregate"]
ordins = ["hundred","thousand","million","billion","trillion","lakh","crore"]
normal = {"one":"first","two":"second","three":"third","four":"fourth","five":"fifth","six":"sixth",
	  "seven":"seventh","eight":"eighth","nine":"ninth","ten":"tenth","eleven":"eleventh","twelve":"twelfth","thirteen":"thirteenth",
	  "fourteen":"fourteenth","fifteen":"fifteenth","sixteen":"sixteenth","seventeen":"seventeenth","eighteen":"eighteenth", 		  "ninteen":"ninteenth","twenty":"twentieth","thirty":"thirtieth","forty":"fortieth","fifty":"fiftieth","sixty":"sixtieth",
	  "seventy":"seventieth","eighty":"eightieth","ninty":"ninetieth","hundred":"hundredth","thousand":"thousandth","million":"millionth",
	  "billion":"billionth","trillion":"trillionth","lakh":"lakth","crore":"croreth"}
endins = ["st","nd","rd","th"]
extras = ["and"]
totalnum = []
totalnum.extend(normal.keys())
totalnum.extend(normal.values())
totalnum.extend(extras)
calender = ["day","days","week","weeks","year","years","month","months","decade","century","decades","centuries"]
yearbox = ["year","years","decade","decades","century","centuries"]
negetive = ["previous","yesterday","before","back","less","earlier"]
positive = ["next","tomorrow","after","forthcoming","later","more"]
daters = []
daters.extend(calender)
daters.extend(yearbox)
daters.extend(negetive)
daters.extend(positive)
stoppers =["a","a's","belongs","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain't",
"all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any",
"anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't",
"around","as","aside","ask","asking","associated","at","available","away","awfully","be","became","because","become","becomes","becoming",
"been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but",
"by","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes",
"concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","currently",
"definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done","down","downwards","during","each",
"edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone",
"everything","everywhere","ex","exactly","example","except","far","few","fifth","first","five","followed","following","follows","for",
"former","formerly","forth","four","from","further","furthermore","get","gets","getting","given","gives","go","goes","going","gone","got",
"gotten","greetings","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's","hello","help","hence","her",
"here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit",
"however","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","indeed","indicate","indicated","indicates","inner",
"insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself","just","keep","keeps","kept","know","known",
"knows","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","little","look","looking",
"looks","ltd","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my",
"myself","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody",
"non","none","noone","nor","normally","not","nothing","novel","now","nowhere","obviously","of","off","often","oh","ok","okay","old","on",
"once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own",
"particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","que","quite","qv",
"rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","said","same","saw","say",
"saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious",
"seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow","someone","something",
"sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t's",
"take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then",
"thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they'd","they'll","they're",
"they've","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too",
"took","toward","towards","tried","tries","truly","try","trying","twice","two","un","under","unfortunately","unless","unlikely","until",
"unto","up","upon","us","use","used","useful","uses","using","usually","value","various","very","via","viz","vs","want","wants","was",
"wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were","weren't","what","what's","whatever","when","whence",
"whenever","where","where's","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who",
"who's","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won't","would","wouldn't","yes","yet",
"you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]
