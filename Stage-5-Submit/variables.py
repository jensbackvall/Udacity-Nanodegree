lesson = [
			[	
				'The Web and Basic HTML',
				['lesson-I-i', 'The Web', """The World Wide Web... what is it really?
				<br>
				As the name suggests, it is a kind of web, where millions of computers are linked up by web-like connections
				through wires, fibres, sattelites etc.
				<br>
				When I turn on my computer and want to access a web page, my computer recieves an HTML document that the browser
				I am using can interpret to show me whatever content that particular page has to show me.
				<br>
				You could say that the <em>line of command</em> looks something like this:
				<br>
				<br>
				<p class="p-center">
					PERSON&lt;-&gt;COMPUTER&lt;-&gt;INTERNET&lt;-&gt;HTTP&lt;-&gt;SERVERS
				</p>
				<br>
				In this example, HTTP is a type of protocol used to connect with servers, and servers are, as we all know, a kind
				of computers, often holding a whole or parts of a web page, online game etc."""],
				['lesson-I-ii', 'Hyperlinks', """Web pages contain hyperlinks and as these can point me toward anything, be it pictures, videos, text, music or any
				combination of these things, one can easily say that the anything can exist on the web, in one form or another.	"""],
				['lesson-I-iii', 'HTML', """HTML or <span class="specialfont-1">H</span>yper <span class="specialfont-1">T</span>ext <span class="specialfont-1">M</span>arkup <span class="specialfont-1">L</span>anguage
				is the basic language of the internet. It contains:
				<br>
				<p class="p-center">
  				HYPERLINKS, references to other content
  				<br>
  				TEXT content, which is basically what you read
 				 <br>
  				MARKUP, defining what the above looks like
  				<br>
  				and it is a LANGUAGE"""],
  				['lesson-I-iv', 'Tags', """The Markup is made up of a load of <em>tags</em>, defining the way the content looks and what it does.
				<br>
				Most tags have an opening and a closing tag which show where it starts and where it ends. If the opening tag is <b>&lt;p&gt;</b>, the ending tag will be <b>&lt;/p&gt;</b>.
				All tags start with a &lt; and end with a &gt;. Thank you to <a href="http://www.boutell.com">boutell.com</a> for showing me how
				to write these in my code without them being a functional tag :-).
				<br>An opening and a 
				closing tag, with text content in between make up what is referred to as an <em>element.</em>
				<br>
				<br>
				Basic tags are the <b>b</b> tag, which makes text come out <b>bold</b> on the screen and the <em>em</em> tag,
				which makes text show up in <em>italics</em>.
				<br>
				<br>
				Some tags are so called VOID tags. This means that they do not have an ending tag. An example is the IMG tag.
				The IMG tag uses the URL of an image and displays it on the page. Here's one that I found with a quick google search. Thanks to 
				<a href="http://imbreannarose.com">imbreannarose.com</a> for this:
				<br>
				<br>
				
					<img src="http://imbreannarose.com/wp-content/uploads/2012/10/html-lessons-img-tag.jpg" class="img-responsive" alt="this should be a neat img poster">
							"""],
  				['lesson-I-v', 'Whitespace', """If you want whitespace on your page, you need to use specific tags for this, as HTML only gives you one space, no matter how many clicks of
				the spacebar you put into your code.
				<br>
				The one which may be the most commonly used (but since my knowledge is limited, I might be wrong about this) <b>br</b> tag, which gives you a
				line-break. The br tag has no ending tag, and using one simply gives you the afore-mentioned line-break.
				<br>
				<br>
				You can also use the <b>p</b> which creates a <b>paragraph</b>. This has an opening and an ending tag and everything in between them is a part of the paragraph.
				<br>
				<br>
				The br tag is a so called <b>inline</b> tag and the p tag is a so called <b>block</b> tag. As I understand it, the inline tag works on the line of text it is in
 				while the block tag creates a kind of <em>invisible box</em> for it's content.
 				<br>
 				Another block element is the <b>div</b> tag while another inline element is the <b>span</b> tag. More on these further down the page."""]
			],

			[
				'HTML, CSS, Editors and Structure',
				['lesson-II-i', 'Why HTML and CSS?', """HTML and CSS are a good introduction to programming, so even if you do not plan on becoming a front end web-developer, this is a great way to start.
				<br>
				<br>
				This is because HTML and CSS are languages that translate directly to a clear, visual result, as opposed to other languages like PYTHON, where other kinds of in-depth understanding of the actual code is needed to understand what it does.
				<br>
				<br>
				A short explanation of what HTML and CSS do could be: Think of your website as a house. The HTML gives you the basic structure, like where the rooms are, and which door leads where. The CSS files are the decoration, determining what the rooms look like."""],
				['lesson-II-ii', 'Editors', """There are many different editors to choose between when writing your code, and you can actually use any text editor or similar program like Word, Pages etc. All you have to do is make sure you use the right syntax and save the document as HTML.
				<br>
				<br>
				But there are better, more specifically suited editors. Here are three of them:
				<br>
				<br>
				<table class="p-center">
					<tr>
						<td>EDITOR:</td>
						<td>Scratchpad.io</td>
						<td>Codepen.io</td>
						<td>Sublime</td>
					</tr>
					<tr>
						<td>LANGUAGES:</td>
						<td>HTML and CSS</td>
						<td>HTML, CSS and Javascript</td>
						<td>All languages</td>
					</tr>
					<tr>
						<td>POWER:</td>
						<td>Less powerful, but beginner friendly</td>
						<td>More powerful and still easy to use</td>
						<td>Powerful with many possibilities that take time to learn</td>
					</tr>
				</table>
				<br>
				An other great tool is the developer tool in Google's Chrome browser. Here's a Udacity video showing how to access it:
				<br>
				<br>
				<p class="p-center">
				<iframe width="560" height="315" src="https://www.youtube.com/embed/_e-gGAM4noQ" allowfullscreen></iframe>
				</p>"""],
				['lesson-II-iii', 'Online Resources', """There are myriads of tags, attributes and more that can be used in HTML and CSS; way too many to remember by heart. And you don't need to! Luckily there are also myriads of online resources where you can look up anything and everything you need.
				<br>
				<br>
				My favourite is definitely
				<a href="www.w3schools.com">WWW.W3SCHOOLS.COM</a>. For example, 
				I wouldn't have been able to make the table in the previous section without it and I've already used it more than 20 times when coding this page. So I'd like to extend a huge thank you to all the people who manage and update that site!!!
				<br>
				<br>
				And to everyone else: If you haven't used it yet, start using it."""],
				['lesson-II-iv', 'Structuring your HTML', """I've already mentioned <b>Inline</b> and <b>block</b> tags, where block tags create an <em>invisible box</em> around their content.
				<br>
				These boxes are the basic framework of a web site and in the HTML document you can define these boxes with the <b>&lt;div&gt;</b> tag.
				<br>
				The web site is basically a series of boxes nested inside boxes, nested inside other boxes etc. In the HTML document this can seen as a <em>tree-like</em> structure of &lt;div&gt;s nested inside &lt;div&gt;s, nested inside &lt;div&gt;s etc.
				<br>
				<br>
				Important: <span class="specialfont-2">Although all boxes are SQUARE, their content can be ANY SHAPE!</span> So everything is square even when nothing is.
				<br>
				<br>
				But all the boxes aren't just &lt;div&gt;s. There can be paragraphs: <b>&lt;p&gt;</b>, tables: <b>&lt;table&gt;</b> and many other tags within the tree.
				<br>
				<br>
				This tree of tags is refered to as the <b>DOM</b> tree, or <span class="specialfont-1">D</span>ocument <span class="specialfont-1">O</span>bject <span class="specialfont-1">M</span>odel tree.
				<br>
				<br>
				When looking at HTML code, you can see the indented structure of the tags, inside tags, inside tags, which is where the term tree comes from, as these look somewhat like an inverted tree, starting with the outer branches to the far left and the bottom of the trunk at the far right. But unlike a tree, the trunk does not control the branches. In the case of HTML, if a tag is nested inside another tag (therefore being further to the right in the HTML document), it is controlled by the tag it is nested inside.
				<br>
				This is refered to as <b><em>inheritance</em></b>. The inherited properties can be controlled with the CSS code.
				<br>
				 More about CSS below."""]
			],

			[
				'CSS Style, Creating the Structure and Checking for Errors',
				['lesson-III-i', 'CSS', """As mentioned earlier, CSS, or <span class="specialfont-1">C</span>ascading <span class="specialfont-1">S</span>tyle <span class="specialfont-1">S</span>heets, controls the style of the HTML or the way it looks.
				<br>
				<br>
				With CSS, you can decide how big the aforementioned <em>invisible</em> boxes are, where they appear on the screen, what shape they are or contain, what colour, border or margin they have, what colour, size, font or other styling text has etc. They are loads of things you can control with the CSS.
				<br>
				<br>
				The great thing about having these things separated from the HTML, is that you can let a single snippet of code in CSS control many big pieces of code in the HTML. This let's you minimize the amount of code you need to accomplish many similar things in many different places on a web site.
				<br>
				<br>
				You do this by giving the
				<b>class</b> name to all HTML elements that you want to give the same look, and asigning the specific class different styles in the CSS file.
				<br>
				I did this with the bold, blue letters in <span class="specialfont-1">C</span>ascading <span class="specialfont-1">S</span>tyle <span class="specialfont-1">S</span>heets, using a class that I've named <em>specialfont-1</em>. Any text assigned this class, using the <b>span</b> tag will show up in this way."""],
				['lesson-III-ii', 'Creating the Structure', """Using the HTML and the assigning CSS correctly can save you a lot of time and bother when doing the initial coding. In addition to this, it makes it easier for you to change general aspects of your sites appearance in an easy way, without having to rewrite almost everything from scratch.
				<br>
				This is done by making sure that all the <em>invisible</em> boxes in your HTML are divided into &lt;div&gt;s that are assigned specific <b>class</b> names.
				<br>
				<br>
				When I wrote the initial code for this page, I started by creating all the containers or &lt;div&gt;s for everything for every element on the page, like <span class="specialfont-3">Lesson1</span>, <span class="specialfont-3">Lesson2</span> and <span class="specialfont-3">Lesson3</span>, with different parts, like <span class="specialfont-3">The Web</span>, <span class="specialfont-3">Online Resources</span> or <span class="specialfont-3">CSS</span> nested inside them.
				<br>
				I did this without putting any content inside them, other than a little place-holder text.Once I had created the entire HTML structure or tree, I started writing the CSS for the different classes and parts of the page.
				After this I put my notes and any other content I wanted to add inside the &lt;div&gt;s.
				<br>
				While filling in the content, I saw where I wanted special text or other styling and created things like the class <em>specialfont-1</em> that I mentioned earlier, to make the text more interesting and readable.
				<br>
				<br>
				This made it possible for me to avoid unnecessary repetition in the code, because the structure was, and is, so easy to read. An important thing when coding. I can now change the look of the page easily, by just changing a few things in the CSS.
				<br>
				<br>
				During this process, I did encounter one or two places where properties had been inherited, so that I had to redefine some things to make sure that they were specific for just one class and not everything within a higher order class."""],
				['lesson-III-iii', 'Checking for Errors', """Even though you are very diligent when coding, you can still make mistakes. These can be checked online by pasting your HTML code into the online validator at <a href="www.validator.w3.org">validator.w3.org</a> or your CSS into the online validator at <a href="https://jigsaw.w3.org/css-validator/validator">jigsaw.w3.org</a>.
				<br>
				<br>
				<p>
    				<a href="http://jigsaw.w3.org/css-validator/check/referer">
        			<img style="border:0;width:88px;height:31px"
            		src="http://jigsaw.w3.org/css-validator/images/vcss"
            		alt="Valid CSS!" />
    				</a>
				</p>"""]
			],

			[
				'Computers, Programming-Interpreting, Monty Python, Python',
				['lesson-IV-i', 'Computers', """Computers are machines, but unlike many other machines they are versatile or <em>UNIVERSAL</em>.
			<br>
			<br>
			Using the example of a toaster, which is also a machine, we can say that a toaster does pretty much one single thing; It toasts bread. It may do it in a variety of ways, making the bread darker or lighter, more or less crispy, but essentially it is heating and slightly burning the bread. Nothing else.
			<br>
			The only way of making a toaster do anything else, would be to hack it's hardware, or re-build it into something else, rendering it rather un-toaster-like.
			<br>
			<br>
			The <em>UNIVERSAL</em> machine, the computer, can basicaly do anything that it is programmed to do. At least anything computational. And as we see through all the many computer programs that most of us use on a daily basis, both for work and recreation, this is quite a lot in very many different ways, from editting video, to playing 3D games, recording and listening to Podcasts and creating the programs that do all of the above.
			<br>
			<br>
			A great thing about computers is the fact that they perform at very high speeds, making possible the multiple, advanced computations needed to perform a variety of taks.
			<br>
			All you need to do is tell the computer what to do and in what order and it will do it for you very efficiently."""],
				['lesson-IV-ii', 'Languages and Interpreting Them', """The way we tell computers what to do, is by writing code in a programming language, which is then interpreted by the computer.
			<br>
			<br> 		
			There are many different programming languages, as I've talked about earlier, concerning HTML and CSS. But <span class="specialfont-2">WHY</span> do we needed invented and constructed languages when we have so many natural languages to choose from?
			<br>
			<br>
			The problem with natural languages is that they are too ambiguous, making them great for poetry, story-telling and just talking, but terrible for telling a computer what to do.
			<br>
			A programming language needs to be unambigious and predicitive, so that a programmer can produce reliable and consistent results when using the language.
			<br>
			<br>
			In addition to this, natural languages are too verbos and we would have to use tons of text to describe things that can be described much more efficiently using a language like Python.
			<br>
			<br>
			Languages like Python are interpreted by the computer using an interpreter. The interpreter itself is a program, written in some language and it enables the computer to understand the directions given in the code. So:
			<br>
			<br>
			The computer interprets a code, creating an interpreter, which in turn interprets some other code. this code may do many different things, as mentioned above."""],
				['lesson-IV-iii', 'Monty Python', """
			<img src="http://i3.kym-cdn.com/photos/images/original/000/671/961/e55.jpg" class="img-responsive" alt="image Monty Python NFSCD">
			
			<br>
			Guido van Rossum, who created PYTHON, named it after the BBC show Monty Python's Flying Circus because he wanted to give it a name that was <em>"short, unique, and slightly mysterious"</em>.
			<br>
			<br>
			<a href="http://en.wikipedia.org/wiki/Monty_Python">Monty Python</a> is, of course, probably the best comedy ever created, so if for some reason you have not watched any of it before, please start now. Or else the Spanish Inquisition might fetch one of their numerous weapons and use it on you."""],
				['lesson-IV-iv', 'Python', """Like any other language, Python has grammar and syntax, making it possible for people to read and write it and computers to interpret it. Below are some important, basic concepts about Python.
			<div class="part-concept">
				<!-- a part of a concept, for better description of something complex. I won't add these to the top menu, since it might make this too "dense"-->
				<div class="part-concept-title">
					<!-- What the class name says:-) -->
					Some Python Expressions
				</div>
				<div class="concept-description">
					The first basic Python statement we have learnt is <span class="specialfont-3">print</span>, where writing the word print, followed by an expression such as a number or a sum, such as <span class="specialfont-3">2 + 2</span> gives us an output on the screen that is equal to the number or sum we have written.
					<br>
					<br>
					So if I write <span class="specialfont-3">print 2 + 2</span>, I will get an output that says <span class="specialfont-3">4</span>.
					<br>
					<br>
					If I want to output text, for example my name Jens B&auml;ckvall, I need to input the code <span class="specialfont-3">print "Jens B&auml;ckvall"</span>, giving me an output that says <span class="specialfont-3">Jens B&auml;ckvall</span>.
				</div>
			</div>
			<div class="part-concept">
				<!-- a part of a concept, for better description of something complex. I won't add these to the top menu, since it might make this too "dense"-->
				<div class="part-concept-title">
					<!-- What the class name says:-) -->
					Some Python Grammar
				</div>
				<div class="concept-description">
					Sometimes, when programming or when trying to access a program, you get an error message. This may be a <em>SYNTAX ERROR</em>.
					<br>
					Syntax errors come up because... there is an error in the syntax. This can be because the code is incomplete or because it contains syntax not covered by Python, which is therefore not interpretable.
					<br>
					<br>
					Python grammar is very strict, ensuring precision.
					<br>
					<br>
					A Python expression can contain other expressions and operators and can be infinitely long, meaning that expressions can contain other expressions for ever unless all expressions are terminated.
					<br>
					<br>
					<b>Below are the basics for arithmetic expressions:</b>
					<br>
					<br>
					<span class="specialfont-4">An expression</span> can be written as a number.
					<br>
					i.e. 0, 1, 2, 3 etc.
					<br>
					<br>
					<span class="specialfont-4">An expression</span> can also be written as an expression, followed by an operator, followed by another expression.
					<br>
					i.e. 1 + 2, where the numbers 1 and 2 are expressions and the + is an operator.
					<br>
					<br>
					<span class="specialfont-4">An operator</span> can be +, -, * or /, giving us the possibility of doing basic maths.
					<br>
					<br>
					So we can create long expressions containing many expressions and operators.
					<br>
					i.e. <span class="specialfont-3">1 + 5 - 8 * 3</span>, which gives us the output -18.
				</div></div>"""]
			],

			[
				'Variables, Strings and Parameters',
				['lesson-V-i', 'Variables', """A variable is a name that can be assigned a value. The name of the variable can be anything you want, as long as it is meaningful to you.
			<br>
			<div class="part-concept">
				<!-- a part of a concept, for better description of something complex. I won't add these to the top menu, since it might make this too "dense"-->
				<div class="part-concept-title">
					<!-- What the class name says:-) -->
					Assinging Variables
				</div>
				<div class="concept-description">
					If I want to asign a value to a variable, I simply define the name of the variable and give it an initial value.
					<br>
					An example could be the variable <span class="specialfont-4">my_age</span> which can be assigned a value. In my case, I am 38 and I want the variable to have this value, so I will write:
					<br>
					<span class="specialfont-4">my_age = 38</span>
					<br>
					<br>
					I now have a varible called <span class="specialfont-4">my_age</span> with the value 38. I can always assign a new value to the variable, giving it a new meaning.
				</div>
			</div>
			<div class="part-concept">
				<!-- a part of a concept, for better description of something complex. I won't add these to the top menu, since it might make this too "dense"-->
				<div class="part-concept-title">
					<!-- What the class name says:-) -->
					= does NOT mean <em>Equals</em>
				</div>
				<div class="concept-description">
					As you can see in the example I have given above, the equals sign <span class="specialfont-4">=</span> does not have the same function here as it does in mathematics. In maths I could write:
					<br>
					<br>
					5 + 7 = 12
					<br>
					<br>
					or
					<br>
					<br>
					5 = 5
					<br>
					<br>
					where the <span class="specialfont-4">=</span> tells us that two values are the same.
					<br>
					<br>
					In Python, and most other programming languages (probably all, but I'm not sure), the <span class="specialfont-4">=</span> acts as a pointer or arrow telling the interpreter to let the variable my_age point to the value 38 so that this value can be used whenever my_age is invoked.
				</div>
			</div>
			<div class="part-concept">
				<!-- a part of a concept, for better description of something complex. I won't add these to the top menu, since it might make this too "dense"-->
				<div class="part-concept-title">
					<!-- What the class name says:-) -->
					Using Variables
				</div>
				<div class="concept-description">
					Variables are very useful in many ways and we have already used variables earlier in this course, when coding CSS. All the properties we have given our HTML through CSS are variables.
					<br>
					<br>
					Basically variables are so useful because they let us do things like:
					<br>
					<ul>
						<li>
							Letting us assign names that make sense to the programmer or the user, making the code easier to understand, use and change.
						</li>
						<li>
							Making it possible for us to change the value of data over time, something which can be very important to the functioning of some programs.
						</li>
						<li>
							Acting as a storage for data that can be quickly and easily changed in one place that may make an impact in many different places.
						</li>
					</ul>
				</div>
			</div>"""],
				['lesson-V-ii', 'Strings', """Strings are defined as a series of letters and or numbers surrounded by single <span class="specialfont-4">'</span> or double <span class="specialfont-4">"</span> quotation marks.
			<br>
			<br>
			So if I want to print a sentence on the screen, I should write the following:
			<br>
			<span class="specialfont-3">print "I just love coding Python."</span>
			<br>
			<br>
			which will output as:
			<br>
			<br>
			I just love coding Python."""],
				['lesson-V-iii', 'Indexing Strings', """I can index the characters in a string using the square brackets <span class="specialfont-4">[</span> and <span class="specialfont-4">]</span> in the following way:
			<br>
			<br>
			<span class="specialfont-4">print "text"[2]</span>
			<br>
			<br>
			In the above example, I am asking the interpreter to output the character in position 2 of the string "text".
			<br>
			When indexing in this way, it is important to remember that the first character has position 0, the second character has position 1 etc. So in the example I just gave, the output will be <span class="specialfont-4">x</span>, as this letter is the third character, which is in position 2.
			<br>
			<br>
			It is also possible to output a sub-string by indexing all letters between two positions in the following way:
			<br>
			<br>
			<span class="specialfont-4">print "text"[1:3]</span>
			<br>
			<br>
			This example outputs <span class="specialfont-4">ex</span>, because it starts at position 1 and ends with the letter before position 3.
			<br>
			<br>
			Finally, it is also possible to index from the end of a string, where the last character has position -1, the second last character has position -2 etc."""],
				['lesson-V-iiii', 'Using .find', """Using the .find function is almost like an inverted version of the indexing described above, but instead of searching for the characters at certain positions in a string, it finds certain characters in a string and returns their position. Something that I guess could be very useful in building a simple text search tool for a word processing program or even in more advanced search engines.
			<br>
			.find works in the following way:
			<br>
			<br>
			<span class="specialfont-4">print "text".find("xt")</span>
			<br>
			<br>
			In the example, we are searching for <span class="specialfont-4">xt</span> in the string <span class="specialfont-4">text</span>.
			The interpreter returns the value <span class="specialfont-4">2</span> as this is the position where we find the sequence of letters we are looking for.
			<br>
			<br>
			In addition, we can also add an extra parameter when using .find, allowing us to decide where in the string our search starts. This is the way it looks:
			<br>
			<br>
			<span class="specialfont-4">print "This text is a text".find("xt", 8)</span>
			<br>
			<br>
			The example returns the value <span class="specialfont-4">17</span> because we started our search at position 8, thus skipping the first occurence of <span class="specialfont-4">xt</span>."""]
			],

			[
				'Functions (or procedures)',
				['lesson-VI-i', 'What is a Function?', """A function (also called a procedure by some) is a piece of code that takes input, uses that input for something and during the course of this something, produces an output.
			<br>
			An example could be a function that performs a mathematical task, such as adding two numbers together and then dividing the result with a third number. We would then be able to use the function as a calculator for any given values of the three numbers."""],
				['lesson-VI-ii', 'Creating and Using Functions', """<div class="part-concept-title">
					Creating a function
				</div>
				<div class="concept-description">
					If we want to create a function, we start by defining it using <span class="specialfont-4">def</span>. After this, we need to give it a <span class="specialfont-4">name</span> followed by parantheses that can contain  <span class="specialfont-4">parameters</span>. The parameters are variables that can be assigned values when we use the function.
					<br>
					N.B. a function does not necessarily have to have any input parameters, if none are needed for whatever it is that you want the function to do.
					<br>
					After the closing parantheses we add a colon<span class="specialfont-4">:</span>.
					<br>
					<br>
					Inside the function, we write the code that tells the function what to do.
					<br>
					Finally, we use <span class="specialfont-4">return</span> to get a result out of the function. It could look like this:
					<br>
					<br>
					<span class="specialfont-4">
						def maths(a, b, c):
						<br>&nbsp;&nbsp;&nbsp;&nbsp;
						result = (a + b) / c
						<br>&nbsp;&nbsp;&nbsp;&nbsp;
						return result
					</span>
					<br>
					<br>
					We now have a functioning function and just need to know how to use it.
				</div>
			<div class="part-concept">
				<div class="part-concept-title">
					Using the function
				</div>
				<div class="concept-description">
					When using this function, we need to input some values for our parameters. In the example I have written, we have three, so we need to choose three numbers. Let's say 1, 2 and 3.
					<br>
					<br>
					We then simply use the <span class="specialfot-4">print</span> statement, asking it to output the result of our function using our chosen parameters, like this:
					<br>
					<br>
					<span class="specialfont-4">
						print maths(1, 2, 3)
					</span>
					<br>
					<br>
					This gives us the output <span class="specialfont-4">1</span> on the screen, which is of course the answer when adding 1 and 2 and then dividing the result by 3.
					<br>
					<br>
					Using a function is refered to as <span class="specialfont-2">calling</span> it.
				</div>
			</div>"""],
				['lesson-VI-iii', 'The Important RETURN Statement', """It is important to use <span class="specialfont-4">return</span>, as mentioned above, since this is the only way we can get something out of our function. So don't forget it! The reason for this is that return tells Python to output whatever it is we are asking it to return.
			<br>
			if you do forget the return statement, the only output you will see is:
			<br>
			<br>
			 <span class="specialfont-4">None</span> """],
				['lesson-VI-iv', 'Using PRINT to debug', """You can always use <span class="specialfont-4">print</span> in your code, if you want to see what is going on.
			<br>
			<br>
			 If, for example, you have a variable that is supposed to change over time, but your code does not seem to give you the expected result or doesn't give any result, adding <span class="specialfont-4">print</span> statements to your code, to let you see what has happend to your variable along the way could be helpful.
			 <br>
			 It could help you see exactly where things have gone wrong in your code, so that you know where to fix it.
			 <br>
			 <br>
			 <span class="specialfont-2">BUT REMEMBER</span> to remove your print statements from the code once you've fixed your bugs!"""],
				['lesson-VI-v', 'Functions for Less Repetition', """Functions are a great tool for less repetition in coding, since you can let the function output something using a set of variables and then let it produce a similar thing with other content-strings, integers etc, using other <em>values</em> for your variables.
			<br>
			<br>
			And once you've defined your function and have seen that it works, you can let it do the same work again and again without ever having to re-define it."""]
			],

			[
				'Control Flow: if and while loops',
				['lesson-VII-i', 'Comparison operators', """To be able to use <span class = "specialfont-2">if, else, while, for</span> and lots of other statements in our code, we have to understand how to use comparison operators like &lt;, &gt;, ==, !=, &lt;=, &gt;=. These return a Boolean value, being either <span class = "specialfont-2">True</span> or <span class = "specialfont-2">False</span>:
			<br>
			<br>
			4 &lt; 5, four is smaller than five, which is True
			<br>
			4 &gt; 5, four is larger than, which it isn't so this would turn out False
			<br>
			4 == 5, four is equal to five, which it isn't either. False
			<br>
			4 != 5, four is not equal to five. True
			<br>
			4 &lt;= 5, four is smaller than or equal to five... True
			<br>
			4 &gt;= 5, four is larger than or equal to five... False
			<br>
			<br>
			I found a nice list of Python operators here: <a href="http://www.tutorialspoint.com/python/python_basic_operators.htm">tutorialspoint</a>.
			<br>
			<br>
			A single equal sign <span class = "specialfont-4">=</span>, is not a comparison operator, as it is used to assign values in the way I have mentioned in earlier notes."""],
				['lesson-VII-ii', 'Boolean Values and Control Flow', """The Boolean binary values of <span class = "specialfont-2">True</span> or <span class = "specialfont-2">False</span> are important when controlling the order in which different parts of a code are executed, called and/or evaluated. This is known as Control Flow.
			<br>
			<br>
			
			<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/George_Boole_color.jpg/220px-George_Boole_color.jpg" class="img-responsive" alt="image of George Boole">
			
			<br>
			Thank you George Boole! 
			<br>
			And here are two Wikipedia links for more in-depth reading:
			<br>
			<br>
			<a href="https://en.wikipedia.org/wiki/Boolean_data_type">Boolean Data Types</a>
			<br>
			<br>
			<a href="https://en.wikipedia.org/wiki/Control_flow">Control Flow</a>"""],
				['lesson-VII-iii', 'if and else statements', """The <span class = "specialfont-2">if</span> statement is a statement that sets up a parameter that has to be met for it to run the code below it. It can be used together with an <span class = "specialfont-2">else</span> statement, giving us the possibility of having alternative code that will run when the if statement's parameters are not met.
			<br>
			Example:
			<br>
			<br>
			<span class = "specialfont-4">def</span> negative_number_check(x):
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;<span class = "specialfont-4">if</span> x &lt; 0:
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return 'it's negative'
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;<span class = "specialfont-4">else</span>:
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return 'it's positive'
			<br>
			<br>
			print negative_number_check(-8)
			<br>
			<br>
			<br>
			The above procedure prints <span class = "specialfont-3">it's negative</span>, since -8 is less than 0.
			<br>
			<br>
			You can have several if statements following each other or nested inside each other, if this is needed to check several different parameters."""],
				['lesson-VII-iv', 'or', """You can use <span class = "specialfont-2">or</span> to compare to compare two or more statements, where the code simply evaluates whether the given statement is True or False. In a version of <a href="https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/m-48667862">Dave's Example</a>, I could write:
			<br>
			<br>
			<span class = "specialfont-4">def</span> is_friend(name):
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;return name[0] == 'D' or name[0] == 'F' or name[0] == 'G'
			<br>
			<br>
			<span class = "specialfont-4">print</span> is_friend('Daniel') this gives us True
			<br>
			<span class = "specialfont-4">print</span> is_friend('Frederik') this gives us True
			<br>
			<span class = "specialfont-4">print</span> is_friend('Gustaf') this gives us True
			<br>
			<span class = "specialfont-4">print</span> is_friend('Peter') this gives us False
			<br>
			<br>
			The code checks if the name that has been used as input, starts with a D or an F or a G."""],
				['lesson-VII-v', 'while loops', """A loop that keeps repeating itself until something is fulfilled. It is important to use some kind of counter in <span class = "specialfont-2">while</span> loops, so that you can keep track of the iterations and make sure that the loop stops once it has found or accomplished whatever it is you're looking for it to find or accomplish. For example:
			<br>
			<br>
			counter = 0
			<br>
			<span class = "specialfont-4">while</span> counter &lt; 11:
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;<span class = "specialfont-4">print</span> counter
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;counter = counter + 1
			<br>
			<br>
			The above loop will print the numbers from 0 to 10, stopping when the the counter reaches a value of 11, which obviously is not smaller than 11 :-)
			<br>
			<br>
			IMORTANT!: The while statement is spelt with a lower case <span class = "specialfont-4">w</span>. When written with a capital <span class = "specialfont-4">W</span>, you will get a syntax error.
			<br>
			<div class="part-concept">
				<div class="part-concept-title">
					break test
				</div>
				<div class="concept-description">
					while loops can be stopped by using a break expression. This works by testing a parameter through an if statement, and if this statement is True, it jumps out of the while loop, cancelling further iterations after the one that caused the if statement to become True.
					<br>
					Example:
					<br>
					<br>
					counter = 0
					<br>
					<span class = "specialfont-4">while</span> counter &lt; 11:
					<br>
					&nbsp;&nbsp;&nbsp;&nbsp;<span class = "specialfont-4">print</span> counter
					<br>
					<span class = "specialfont-4">&nbsp;&nbsp;&nbsp;&nbsp;if</span> counter == 9:
					<br>
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break
					<br>
					&nbsp;&nbsp;&nbsp;&nbsp;counter = counter + 1
					<br>
					<br>
					The above code would do the same as letting the while loop only go up to x &lt; 10, so it is a pretty dumb use of the break, but it gives the general picture of what it does.
					<br>
				</div>
			</div>"""]
			],

			[
				'Debugging',
				['lesson-VIII-i', 'More Debugging Advice', """Python returns error-messages, called Tracebacks. An example from the lesson is:
			<br>
			<br>
			<span class = "specialfont-2">TypeError: unsupported operand type(s) for +: 'int' and 'str'</span>
			<br>
			<br>
			A good start, when dealing with an error message that you don't understand, is to copy-paste it into a search engine, to see if others have had the same problem and how this can help you understand and correct the error. When looking up the error-message above, I found out that I had to change an integer into a string, by adding str(). 
			<br>
			<br>
			Below are some other debugging tips.
			<br>
			<br>
			<div class="part-concept">
				<div class="part-concept-title">
					Copied code
				</div>
				<div class="concept-description">
					If you have copied code from somewhere, make sure that the code you have copied, does what you want it to do and make sure that you understand it, so that the original code, or your re-working of it, does not contain errors.
				</div>
			</div>
			<div class="part-concept">
				<div class="part-concept-title">
					Using <span class = "specialfont-4">print</span>
				</div>
				<div class="concept-description">
					As I have mentioned earlier, using the print statement is a good way of understanding code and finding out where what has gone wrong.
				</div>
			</div>
			<div class="part-concept">			
				<div class="part-concept-title">
					Editing out or Saving
				</div>
				<div class="concept-description">
					If you have coded something that does not work, don't just throw it out by deleting it. Try editing it out by using a hashtag <span class = "specialfont-4">#</span> in front of it. This way, you can compare the code that didn't work with the code you write afterwards. Maybe you can use some of the old code, or maybe you can learn something for future coding.
					<br>
					<br>
					You may also want to save old code in a separate file, if editing it out takes up too much space, or you just don't want to do it that way.
				</div>
			</div>
			<br>"""]
			],

			[
				'Structured data: List and for loops',
				['lesson-IX-i', 'Strings and Lists: structuring data', """The difference between defining a string and a list, is that a string is a sequence of characters and a list is a sequence of anything.
			<br>
			You can index both strings and lists in similar fashions.
			<br>
			Examples:
			<br>
			<br>
			s = 'Hello!World'
			<br>
			<br>
			p = ['H', 'e', 'l', 'l', 'o', '!']
			<br>
			<br>
			indexing either the string s or the list p will give the same result at the same positions.
			<br>
			Examples:
			<br>
			<br>
			s[4] gives us the letter o and so does p[4].
			<br>
			<br>
			A cool thing about lists is that they can contain <b>both</b> strings and numbers and can even contain other lists, like:
			<br>
			<br>
			H2G2 = ['The answer to the great question', 42, 'Adams', ['Earth', 'Earth mach 2', 'Slartibartfast']]
			<br>
			<br>
			A list contained inside another list is referred to as a nested list.
			<br>
			When creating large lists, you should be aware of where you break the list (this should be after a comma). It is also a good idea to create indentation, so that the entire list is indented equally.
			<br>
			<br>
			Lists nested inside other lists can be indexed by using double brackets, like:
			<br>
			<br>
			H2G2[3][2], which will return the name Slartibartfast"""],
				['lesson-IX-ii', 'Mutating and Aliasing', """Strings are immutable, meaning that you can't change them directly.
			<br>
			Lists are mutable, meaning that we can reassign new values to elements in the list. This is important, as we have to be aware of what variables point to, and how they may change, the same list.
			<br>
			<br>
			When re-assigning a variable containing a string, the variable is simply pointed toward a new value as in the example below.
			<br>
			<br>
			Initial value:
			<br>
			s = 'Hello'
			<br>
			re-assigning:
			<br>
			s = 'Yello'
			<br>
			<br>
			s now points to the value 'Yello'  but it has not mutated.
			<br>
			<br>
			If we do the same with a list, we can do the following;
			<br>
			<br>
			Initial value:
			<br>
			p = ['H', 'e', 'l', 'l', 'o']
			<br>
			re-assigning:
			<br>
			p[0] = 'Y'
			<br>
			<br>
			then we let a new variable point to p. We call it q.
			<br>
			<br>
			q = p
			<br>
			<br>
			q and p are now linked and when we change a value in q.
			<br>
			<br>
			q[0] = 'T'
			<br>
			<br>
			the same value is changed in p, so now both lists, when printed, look like this:
			<br>
			<br>
			['T', 'e', 'l', 'l', 'o']
			<br>
			<br>
			This is referred to as aliasing. So two or more aliased lists always change together when one is changed."""],
				['lesson-IX-iii', 'List Operations', """Here are three different list operations that are useful to know.
			<br>
			<div class="part-concept">		
				<div class="part-concept-title">
					append
				</div>
				<div class="concept-description">
					This mutates the list by adding a new object to a list. Example;
					<br>
					<br>
					<u>We have a list called p, containing the numbers from 0 to 3 like this:</u>
					<br>
					<br>
					p = [0, 1, 2, 3]
					<br>
					<br>
					<u>We then use append to add 4 to the list like this:</u>
					<br>
					<br>
					p.append(4)
					<br>
					<br>
					<u>If we print p now, it looks like this:</u>
					<br>
					<br>
					[0, 1, 2, 3, 4]
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					+
				</div>
				<div class="concept-description">
					<u>This concatenates two lists (without mutation) in the following way:</u>
					<br>
					<br>
					[0, 1] + [2, 3]
					<br>
					<br>
					These two lists have now been used to create a new list which looks like [0, 1, 2, 3]. As mentioned, the original lists have not mutated while producing the new list.
					<br>
					<br>
					<u>We can also use the assignment syntax += which works just like append, in that it adds to a list. For example:</u>
					<br>
					<br>
					mylist = [1, 2, 3, 4]
					<br>
					mylist += [5, 6]
					<br>
					<br>
					After the above, mylist now has the value [1, 2, 3, 4, 5, 6]
				</div>
			</div>
			<div class="part-concept">
				<div class="part-concept-title">
					len
				</div>
				<div class="concept-description">
					<u>Counting a list with len:</u>
					<br>
					<br>
					len([0, 1]) gives us 2, as there are two objects in the list.
					<br>
					<br>
					<u>Counting a list with nested lists counts the objects in the outermost list:</u>
					<br>
					<br>
					len(0, 1, [2, 3]) gives us 3, as there are three objects in the outermost list.
					<br>
					<br>
					<u>When using len on a string, it counts the characters in the string, like this:</u>
					<br>
					<br>
					len('four') gives us 4, as there are four characters in the word.
					<br>
					<br>
					<br>
					Important! Len applies two other things than just lists. Anything(I think) that contains a number of values/integers/strings/objects can be counted with len.
				</div>
			</div>"""],
				['lesson-IX-iv', 'for loops', """A loop that, unlike a while loop, does not need a counter. If I want to print the numbers in a list p, I'd do it the following way(first defining the list):
			<br>
			<br>
			p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
			<br>
			<span class = "specialfont-4">for</span> element <span class = "specialfont-4">in</span> p:
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;<span class = "specialfont-4">print</span> element
			<br>
			<br>
			The above loop looks in the list p and prints the first element, whereupon it moves forward to the next element, stopping it's iterations when it has gone through the whole list. Pretty smart and very good for avoiding infinite loops, which can cause problems in your code.
			<br>
			<br>
			Advice: Always use a for loop, if you can. Only use while loops if you have to and make sure that you create a statement that ends the while loop when you need it to end.
			<br>
			<div class="part-concept">		
				<div class="part-concept-title">
					range(x)
				</div>
				<div class="concept-description">
					When using for loops, the operation <span class = "specialfont-4">range</span> is a great tool for choosing the number of your iterations. It works by giving it a number, whereupon it goes from 0 (zero) up until, but not including, the number. Example:
					<br>
					<br>
					range(25) will give us 25 counts from 0 to 24.
					<br>
					<br>
					<u>So a for loop could be:</u>
					<br>
					<br>
					<span class = "specialfont-4">for</span> element <span class = "specialfont-4">in</span> range(25):
					<br>
					&nbsp;&nbsp;&nbsp;&nbsp;print 'number' + str(element)
				</div>
			</div>"""],
				['lesson-IX-v', 'Indexing', """<br>
			<div class="part-concept">		
				<div class="part-concept-title">
					indexing with <span class = "specialfont-4">.index</span>
				</div>
				<div class="concept-description">
					&lt;list&gt;<span class = "specialfont-4">.index</span>
					<br>
					<br>
					if &lt;value&gt; is found in the &lt;list&gt;, the position of the first occurrence is returned. If it is not, an error is produced.
				</div>
			</div>
			<div class="part-concept">		
				<div class="part-concept-title">
					indexing with <span class = "specialfont-4">in</span>
				</div>
				<div class="concept-description">
					written in the following way:
					<br>
					<br>
					&lt;value&gt; <span class = "specialfont-4">in</span> &lt;list&gt;
					<br>
					<br>
					This procedure checks if &lt;value&gt; occurs in the &lt;list&gt;. If it does, we get the output True. If not, we get the output False.
					<br>
					<br>
					We can also use <span class = "specialfont-4">not in</span>, like this:
					<br>
					<br>
					&lt;value&gt; <span class = "specialfont-4">not in</span> &lt;list&gt;
					<br>
					<br>
					Similarily, it produces either False or True, depending on whether the &lt;value&gt; does not occur in the &lt;list&gt;.
				</div>
			</div>"""]
			],

			[
				'Solving Problems',
				['lesson-X-i', 'Some Notes on Problem-Solving', """<div class="part-concept">
				<div class="part-concept-title">
					Dave's short 101:
				</div>
				<div class="concept-description">
					<ol type = "0">
						<li><span class = "big_friendly_letters">DON'T PANIC</span></li>
						<li>What are your inputs?</li>
						<li>What are your desired outputs?</li>
						<li>Try some examples by hand.</li>
						<li>Can you think of a simple, mechanical solution?</li>
						<li>Develop your solution step, by step, testing as you go.</li>
					</ol>
				</div>
			</div>
			And here is my own, not as short, add-on, to go after the 101 above:
			<br>
			<ol type = "0">
				<li>Find relationship between possible inputs and desirable outputs.</li>
				<li>What are the possible inputs?... understand them. What are the desired outputs or types of output?</li>
				<li>Defensive programming: Thinking about possible mistakes that can be made in inputs and write code to check for these.</li>
				<li>Understand the outputs.</li>
				<li>Try some examples to make sure that you really understand what a set of inputs should output.</li>
				<li>Consider how you would solve the problem, as a human. If you don't know how to solve it through systematic thinking, you probably can't solve it through coding.</li>
				<li>Try writing <i>pseudo-code</i> to see what you have to code.</li>
				<li>After creating your <i>pseudo-code</i>, think about if there might be more simple, mechanical ways of solving the problem.</li>
				<li>It is important to be able to write small bits of code and understand what they do to be able to make problem-solving progress.</li>
				<li>ALWAYS CHECK YOUR INDENTATIONS!!!!!!!!! I write this with capitals, because I have failed at least two example problems due to creating faulty indentation.</li>
			</ol>"""]
			],

			[
				'Abstraction and OOP',
				['lesson-XI-i', 'Abstraction, a short introduction', """Abstraction can be described as a way of collecting lots of basic information or instructions into groups, where these instructions combine to become something more or other than the instructions themselves.
			If I say the word house, you know what kind of structure I am probably referring to, and I don't need to describe every aspect of the house. So instead of describing the foundation, the bricks, the boards, the windows, the doors etc, I just have to say house.
			<br>
			<br>
			When we talk about abstraction in a programming language like Python, we talk about the built in functions that can be used, although we don't actually have to (exactly) know or control how they work. We just use them and control how they are used, enabling us to do more things in less time, thanks to the pre-programmed functions. These functions are a part of Python, through the Python Standard Library. This video from the course explains the basics in a nice and easy-to-understand manner:
			<br>
			<br>
			<p align = "center">
				<iframe width="560" height="315" src="https://www.youtube.com/embed/5TGY5p07g6M" frameborder="0" allowfullscreen></iframe>
			</p>
			<br>
			<br>
			For example:
			If I want to draw a shape with Python's built-in <span class = "specialfont-2">turtle</span>, I only have to tell the turtle where to go, without having to know what the turtle tells the computer to enable it to draw pixels on the screen.
			<br>"""],
				['lesson-XI-ii', 'DRY', """
			<img width="750" height="450" src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Drought.jpg" class="img-responsive" alt="image of drought">
		
			<br>
			Why is the land so barren and dry? Maybe because all of the resources were over-used through unnecessary repetition... so...
			<br>
			<br>
			<p class="p-center">
			<span class = "specialfont-1">D</span>on't <span class = "specialfont-1">R</span>epeat <span class = "specialfont-1">Y</span>ourself!!!
			</p>
			<br>
			Avoiding repetition is very important for a number of reasons. Some of them being; readability, bug-checking, use of memory etc.
			<br>
			<br>
			As in most coding, repetition is a bad thing as it can lead to all sorts of problems (see above ;-) ).
			The use of classes and objects and the way that Object-Oriented Programming(OOP) let's the code use and re-use itself and other related bits of code in different modules is a great way to avoid doing things again and again.
			<br>
			<br>
			This also makes OOP a fantastic tool for programming on a large scale, as we can re-use our own code, as well as accessing code made by other's, including that available in the Python Standard Library and in add-ons like the Twilio API(Application Programming Interface).
			<br>
			Thanks to this, we can do big things, without having to create miles of code from scratch."""],
				['lesson-XI-iii', 'OOP, A Short Introduction', """<div class="part-concept">	
				<div class="part-concept-title">
					OOP - A Definition
				</div>
				<div class="concept-description">
					Object-Oriented Programming (OOP) is a programming paradigm where the focus is on <span class = "specialfont-3">objects</span> and <span class = "specialfont-3">data</span>.
					<br>
					<br>
					This is in contrast to programming where the focus is on <span class = "specialfont-3">logical procedures</span> that take <span class = "specialfont-3">input data</span> and performs some action with it, to produce <span class = "specialfont-3">output data</span>.
					<br>
					<br>
					So in OOP, we don't start by defining logical procedures to handle our data, <b>we start by defining our data</b>. Once we know what data we want to manipulate and how we want to manipulate it, we also have to know how the different types of data relate to each other.
					<br>
					<br>
					This is where we create our <span class = "specialfont-3">objects</span>. Each object is structure containing data (attributes) and <span class = "specialfont-3">methods</span> that can use and manipulate the data.
					<br>
					Similar objects are refered to as <span class = "specialfont-3">instances</span> of a <span class = "specialfont-3">class</span>. A class definition can be re-used indefinitely to create as many instances as we want to.
					<br>
					<br>
					Once we have defined and created our objects and the logical methods they contain, these objects can call, use and even modify each other.
					<br>
					<br>
					So, OOP can be loosely defined as a series of objects(data containers) that use each other to create the large complex structure that is the program.
					<br>
					<br>
					Here are two links for more reading on OOP:
					<br>
					<a href="https://en.wikipedia.org/wiki/Object-oriented_programming">Wikipedia</a>
					<br>
					<a href="http://searchsoa.techtarget.com/definition/object-oriented-programming">Techtarget</a>
				</div>
			</div>
			<br>
			Why is OOP a good tool for efficient programing?
			<br>
			In Object-Oriented Programming, we work with classes and objects. These classes and objects contain data that can be used by other classes and objects that call each other, thus enabling us to store information in one class that can be used by many classes and objects. This makes the code shorter(because of less repetition), helps us avoid making the same mistakes in multiple places and makes it easier for us to update the code, without having to make too many changes in many different places.
			<br>
			<br>
			We can talk about classes as being basic blueprints that can be used over and over again. We use the blueprints to create other classes and objects that have all or some of the same properties. Just like I wrote  above in <a href="#lesson-VI-v">Functions for Less Repetition</a>.
			<br>
			<br>
			<div class = "part-concept">
				<div class="part-concept-title">
					Reasons why OOP is good for large programming projects
				</div>
				<div class = "concept-description">
					When coding large, complicated programs, the programmers will be defining and re-defining enormous amounts of variables and functions.
					<br>
					These variables and functions will be used and modified by each other and when the code is updated, they might even be modified by programmers.
					<br>
					<br>
					Imagine if 2, 5, 10 or even more coders are working on this program, where the variables and functions are not split into separate modules, objects and instances. They all have to make sure that they know what every single variable and function (and there may be thousands or tens of thousand) does and what they can control, call and modify.
					<br>
					This is probably <b>impossible</b> for all but an almost non-existent sub-set of the human species, which leads us towards almost certain bugs that are very, very difficult to find.
					<br>
					<br>
					But <span class = "big_friendly_letters">DON'T PANIC</span>, OOP is here.
					<br>
					Using OOP, the many variables and functions are contained inside objects and classes, some of which can't even call each other, if they are not supposed to. These objects can (and should) have names that make it easy for anyone to see what they are doing, so that altering the code becomes less difficult for anyone knowing the language.
					<br>
					Using OOP, everything is not one big file with over 100000 lines of code, but is split into many smaller objects that are easily manageable. These objects are easier to control, making it easy to avoid bugs and easier to find them if, and when, they do pop up.
					<br>
					<br>
					Another (but in a way it is more of what I mentioned above) great thing about OOP, when it comes to large projects, is the way you can use <i>abstraction layers</i>, both through built-in modules or new modules that you create yourself.
					<br>
					This let's you define certain functionality and then lock this functionality into it's own little <i>box</i> that is simply called when it is needed. If somehting goes wrong or has to be changed, you open the <i>box</i>, make your changes and close it again.
					<br>
					You are basically hiding all but the most necessary information about the object in the box, making it easier to use and easier for other programmers to understand, use and potentially modify.
				</div>
			</div>
			<br>
			So, in OOP we define classes that control multiple instances in the code, just like earlier on in the course where we used <a href="#lesson-III-i">CSS</a> to create classes that control many different aspects of our HTML, in many different places. 
			<br>
			<br>
			As a matter of fact, CSS has even more in common with OOP, as many of the traits defined for an element in CSS, will be inherited by children of this element, much in the same way that classes in Python inherit from their parent-classes. So if you have a div that has been assigned a specific font and text-alignment, any div inside this first div will inherit the font and alignment, without this being assigned in that div.
			<br>
			But not all traits are automatically inherited by the child element, if this is not explicitly done in the code. Border and padding properties are not, but there are options for making this happen.
			Here is an interesting, albeit quite old, post about this: <a href="http://webdesignfromscratch.com/html-css/css-inheritance-cascade/">webdesignfromscratch</a>.
			<br>"""]
			],

			[
				'Using Built-in Functions',
				['lesson-XII-i', 'Importing Modules and Functions', """Python has many built in <span class = "specialfont-2">modules</span> that can be used to perform a variety of tasks/functions.
			<br>
			Things like <span class = "specialfont-2">turtle</span>, <span class = "specialfont-2">time</span>, <span class = "specialfont-2">webbrowser</span> and many others. The modules contain functions that we can use in many different ways, as described above in the introduction to abstraction.
			<br>
			To use one or more of these functions, we need to import the relevant module(s) into our program, by using the import statement, like this:
			<br>
			<br>
			<span class = "specialfont-4">import</span> turtle
			<br>
			<br>
			turtle has now been imported into the program and can be used.
			<br>
			<br>
			As mentioned earlier, we can also install and import code from outside the Python Standard Library, like the Twilio API.
			<br>"""],
				['lesson-XII-ii', 'Reading About Functions', """To find out more about built in functions, read about the ones you want to use or maybe find new ones that do something you need, you can look them up in the <a href="https://docs.python.org/2/library/">Python Standard Library(PSL)</a>.
			<br>
			<br>
			But remember that finding a certain functionality is probably easier through searching directly in a search engine. That way you'll be able to find the relevant modules and functions, and see examples of how they are used. Then you can go to the PSL to get more in-depth knowledge of the things you are using.
			<br>
			<br>
			Here's a direct link to the turtle module  in the PSL: <a href="https://docs.python.org/2/library/turtle.html">turtle module</a>.
			<br>"""]
			],

			[
				'Classes',
				['lesson-XIII-i', 'Calling and Using a Class', """Once we have imported the module turtle, we can use it to call a class, and in doing this we are in fact initiating a function. There are many classes within turtle, like <span class = "specialfont-2">Turtle</span>, <span class = "specialfont-2">Screen</span> etc.
			<br>
			<br>
			This function is defined inside the class Turtle, and is called __init__(). The __init__() function is referred to as a constructor. 
			<br>
			<div class="part-concept">	
				<div class="part-concept-title">
					Note on constructor/initiator
				</div>
				<div class="concept-description">
					It has to be noted that many online resources say that it is not a true constructor, but only functions as such. These resources and people often call __init__() an initiator, saying that the construction occurs when the class is defined.
					<br>
					<br>
					Here is a link to a StackOverflow question about this: <a href = "http://stackoverflow.com/questions/6578487/init-as-a-constructor">__init__ as a constructor?</a> 
				</div>
			</div>
			<br>
			The __init__() function creates space in our computer's working memory for instances of the class Turtle. In the example below, we are defining brad and britt, which are both instances of the class Turtle:
			<br>
			<br>
			brad = turtle.Turtle
			<br>
			britt = turtle.Turtle
			<br>
			<br>
			So the class, Turtle, is like a basic blueprint within the module turtle that can be used to create multiple instances of the class.
			<div class="part-concept">	
				<div class="part-concept-title">
					Note on capitalization of classes
				</div>
				<div class="concept-description">
					An important thing to remember when using turtle is that the classes Turtle (turtle.Turtle) or Screen (turtle.Screen) must be capitalized. If you write turtle.screen, with a non-capital s, it will produce the following error:
					<br>
					<br>
					<span class = "specialfont-3">AttributeError: 'module' object has no attribute 'screen'</span>
				</div>
			</div>"""],
				['lesson-XIII-ii', 'Creating Classes', """Why create a class?
			<br>
			Although many things are defined within the PSL, specifics aspects of a program that you want to create will not be covered and you have to create classes for yourself.
			Maybe you want to be able to call, see or in other ways use many different objects that are all of the same type. Like in the movie example, where we all know what a movie is and that many different movies exist. 
			<br>
			<br>
			So what should you think about when creating a class?
			<br>
			What aspects of the class are things that all instances of the class have in common, and which of these would it be useful to be aware of, so that we can use them when creating instances of the class?
			<br>
			Again, if we take the movie example, all movies(as far as I know) have a title, a storyline, a trailer, a poster etc. All of these are things that we may want to use for every instance of the class movie, but we don't want to waste time, space and common sense by re-creating all the aspects of a movie every time we define a new movie.
			<br>
			<br>
			Creating the class
			<br>
			When creating the class, we use the Python keyword <span class = "specialfont-4">class</span>, like this:
			<br>
			<br>
			<span class = "specialfont-4">class</span> Name_of_class():
			<br>
			<br>
			This is followed by <b>def __init__()</b>, also known as the <i>constructor</i>, although not everyone agrees upon this(see above).
			<br>
			<br>
			__init__() uses some terms, i.e. __init__(self, a, b, c, etc). More specifically:
			<br>
			<br>
			self: this is for the object being created, so it points to the instance being created. In the movie example, this instance could be <i>The Matrix</i>, <i>Stranger Than Fiction</i> or any other movie that we choose to create an instance for.
			<br>
			<br>
			a, b, c, etc:  are <i>instance variables</i> needed for the specific class we are creating. In the movie example we have title, storyline etc. These should have corresponding names, such as movie_title, movie_storyline, movie_poster etc, rather than having ambiguous names like a, b and c.
			<br>
			<br>
			So if we want to create the class Movie, and want to let it have the three instance variables above, we do it like this:
			<br>
			<br>
			class Movie():
			&nbsp;&nbsp;&nbsp;&nbsp;def __init__(self, movie_title, movie_storyline, movie_poster):
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.title = movie_title
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.storyline = movie_storyline
			<br>
			&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.poster = movie_poster
			<br>
			<br>
			Notice that the first letter in the class Movie is capitalized. This is not obligatory, but is good form as seen in the <a href="http://google-styleguide.googlecode.com/svn/trunk/pyguide.html">Google Style Guide</a>.
			<br>"""],
				['lesson-XIII-iii', 'More on Important Terms', """As we have seen, OOP in Python uses some terms that are important to remember. I've listed some of them below, including ones that I have already explained in the notes above.
			<br>
			<br>
			I'd like to start by adding Kunal's excellent screenshot, showcasing important terms used when creating and using a class.
			<br>
			<br>
				<img src="http://s23.postimg.org/tlvgsbiqz/Screen_Shot_2014_04_18_at_4_52_12_PM.png" class="img-responsive" alt="img tag image">
			<br>
			<div class="part-concept">	
				<div class="part-concept-title">
					Module
				</div>
				<div class="concept-description">
					A module is a file containing Python definitions and statements, essentially a Python program. The file is saved as a Python file, ending in <b>.py</b>.
					<br>
					Modules and the functions defined in a module can be imported into other modules and be used there.
					<br>
					In the screenshot above, <i>media.py</i> is a module and the module <i>webbrowser</i> has been imported into that module.
					<br>
					<br>
					There are numerous built-in modules that can be used for many different things.
				</div>
			</div>
			<div class="part-concept">
				<div class="part-concept-title">
					Objects
				</div>
				<div class="concept-description">
					An object is a structure containing data (attributes) and coding functions (methods) that can use and manipulate the data.
					<br>
					<br>
					Objects can call, use and manipulate each other.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Class
				</div>
				<div class="concept-description">
					A class can refer to a built in class in one of Python's modules or a class created by a programmer.
					<br>
					<br>
					Classes are a kind of blueprint that contain data and functions that control behaviour. They can be used to create multiple instances with different names but the same basic properties. In the screenshot, Movie is a class while Toy_Story and Avatar are instances of the class.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Method
				</div>
				<div class="concept-description">
					A method is a procedure, that does something inside a class or instance.
					<br>
					<br>
					An example is the procedure that opens a browser window, as seen in the screenshot above. see Instance Method below.
					<br>
					<br>
					The <b>def __init__</b> that constructs/initiates the class is also a method.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Constructor
				</div>
				<div class="concept-description">
					A constructor is a method, used to initiate and create memory for an object. The object being a new instance of a class.
					<br>
					<br>
					See more on the __init__ in <a href="#lesson-XIII-ii">Creating Classes</a> further up in the notes.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					self
				</div>
				<div class="concept-description">
					Self is the fixed parameter in a class constructor that points to the class object being created.
					<br>
					<br>
					So if I have a class Movie, as seen above, self points to an instance of that class, be it Toy_Story or Avatar.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Instances
				</div>
				<div class="concept-description">
					An instance is an object created using a class. The instance uses the properties and methods of the class, but can also have unique properties of it's own.
					<br>
					<br>
					In the screenshot above, the class Movie has been used to create the instances Toy_Story and Avatar.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Instance Variables
				</div>
				<div class="concept-description">
					Instance variables are variables defined within a class. These variables are used to define certain aspects of the of the class.
					<br>
					The instance variables all point to self(mentioned above) and are probably, but not necessarily, unique for each instance.
					<br>
					<br>
					In the screenshot above, we can see that the instance variables tell us different things about Movie, like the title, storyline etc. And when we create Toy_Story or Avatar we define, and store in memory, the different values of the variables for each of these two instances.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Instance Methods
				</div>
				<div class="concept-description">
					An instance method is a method within a class, used to enable each instance of the class to do the same thing. Much like instance variables, only with a specific function rather than just an integer or string value.
					<br>
					<br>
					Again, the screenshot above gives us the <b>webbrowser.open</b> example, where this method can be used by both Toy_Story and Avatar, to open their trailer in a webbrowser.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Class Variables
				</div>
				<div class="concept-description">
					A class variable is similar to an instance variable, in that it is shared by all instances of the class. BUT! It is defined outside any method's of the class. This means that it is an attribute of the class, but not an attribute of an instance of the class, compared to the instance variables above, where we can see that self.title and self.storyline are attributes of every instance of the class.
					<br>
					<br>
					In other words, a class variable is almost not a variable for the instances of the class, since it will always be the same for all instances. If it is changed and get's a new value of some kind, this value will change for all instances of the class. But it is, of course, a variable, since it's value can be changed.
					<br>
					<br>
					Python has some pre-defined class variables or <i>class attributes</i>, one of them being <b>__doc__</b>. This can be used to supply some kind of documentation for the class you have created, so that potential users can see what it does, quickly and easily. Adding a __doc__ class variable to your class can be done like this:
					<div class = "part-concept">
						<span class = "specialfont-2">class</span> Nothing_special(object):
						<br>
						&nbsp;&nbsp;&nbsp;&nbsp;&quot;&quot;&quot;This class does nothing special&quot;&quot;&quot;
						<br>
					</div>
					Other pre-defined class variables are __name__, __dict__, __bases__ and __module__.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Class Methods
				</div>
				<div class="concept-description">
					I mention these only because I felt curious about them, although we haven't gone through the subject of class methods.
					<br>
					<br>
					I'm actually not completely sure how class methods work. It seems intuitive that they call on a class, rather than instances of the class, but other than this, it seems to me that the use of class methods is above my current knowledge of programming.
					<br>
					I found mention of meta-models on wikipedia <a href="https://en.wikipedia.org/wiki/Class_method#Class_methods">here</a>, but this is clearly too advanced for me at the moment.
					<br>
					<br>
					I'm looking forward to getting to a level where I understand it.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Inheritance
				</div>
				<div class="concept-description">
					The term <i>inheritance</i> deals with the fact that we can create subclasses that are children of other classes and inherit their or some of their properties from a parent class.
					<br>
					<br>
					If we have a parent class called Family_members with properties such as name, age etc, then we can have subclasses(children) of the class Family_members that could be Adults, Kids and Pets. These three subclasses can all inherit the properties of name and age, but can also have uniques properties of their own. Maybe the Adults have a job property, the Kids have a favourite_toy property and the Pets have a species property.
					<br>
					<br>
					A person who does a good job of explaining inheritance in an easy way is <a href="http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/">Jess Hamrick</a>.
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Method Overriding
				</div>
				<div class="concept-description">
					Method overriding is when you create a new method in a child class that overrides, or replaces, a corresponding method in a parent class.
					<br>
					<br>
					The overriding method has the same name as the method in the parent class.
					<br>
					<br>
					An example could be that we have created the parent class Family_members:
					<div class = "part-concept">
						<span class = "specialfont-2">class</span> Family_members(object):
						<br>
						&nbsp;&nbsp;&nbsp;&nbsp;<span class = "specialfont-2">def</span> __init__(self, name, age, category):
					</div>
					<br>
					And we then create the child class adult:
					<div class = "part-concept">
						<span class = "specialfont-2">class</span> Adult(Family_members):
						<br>
						&nbsp;&nbsp;&nbsp;&nbsp;<span class = "specialfont-2">def</span> __init__(self, name, job):
					</div>
					<br>
					Here, the <b>def __init__</b> method in Adult, overrides the <b>def __init__</b> method in Family_members. This doesn't mean that the parent's method is no longer functional, it just means that some of the things it does are overruled by the child's method.
					<br>
					If we still want to make sure that the things initiated in the parent are used in the child, we can simply call the parent like this:
					<div class = "part-concept">
						<span class = "specialfont-2">class</span> Adult(Family_members):
						<br>
						&nbsp;&nbsp;&nbsp;&nbsp;<span class = "specialfont-2">def</span> __init__(self, name, job):
						<br>
						&nbsp;&nbsp;&nbsp;&nbsp;Family_members.__init__(self, name, age, "adult")
					</div>
				</div>
			</div>
			<div class="part-concept">	
				<div class="part-concept-title">
					Subtype Polymorphism
				</div>
				<div class="concept-description">
					In Python, polymorphism refers to the fact that Python code can adapt to different types of data input. A proper definition seems to be quite long and complicated, so I'll leave that for the pro's until I fully understand the more intricate aspects myself.
					<br>
					<br>
					But when readig about inheritance I came across the term <i>Subtype Polymorphism</i> several places, so I'd like to mention it.
					<br>
					As I understand it, when a child object inherits from it's parent object, it(the child) can be used and handled by programs that can handle the parent object.
					<br>
					i.e. the code does not have to be designed to handle the child, because the child is a sub-class of the parent and therefore adheres to the rules that makes it possible for the code to handle the parent.
				</div>
			</div>
			<br>
			In researching the above information I used the course material, but also searched and read articles on the following sites:
			<br>
			<br>
			<a href="https://en.wikipedia.org/wiki/Class_method#Class_methods">Wikipedia</a>
			<br>
			<a href="http://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide">toptal.com</a>
			<br>
			<a href="https://docs.python.org/2/tutorial/classes.html">Python Software Foundation</a>
			<br>
			<a href="http://www.tutorialspoint.com/python/python_modules.htm">tutorialspoint.com</a>
			<br>
			<a href="http://stackoverflow.com/questions/18955141/what-is-a-constructor-and-what-does-it-do">stackoverflow.com</a>
			<br>
			<a href="https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods">julien.danjou.info</a>
			<br>
			<a href="http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/">jesshamrick.com</a>
			<br>
			<a href="http://lgiordani.com/blog/2014/08/21/python-3-oop-part-4-polymorphism/">lgiordani.com</a>
			<br>
			<br>
			And probably quite a few more that I haven't bookmarked and haven't got in my recent browser history.
			<br>"""]
			],

			[
				'Networks',
				['lesson-XIV-i', 'What is a Network?', """Networks 101:
<br>
<ul>
	<li>A network is a group of entities that can communicate, even though they are not all directly connected.</li>
	<li>If all nodes in the group can communicate directly, they are not considered a network.</li>
	<li>If two or more nodes communicate through a third node without being in direct contact with each other, all of these nodes are considered to be a network.</li>
</ul>
To create and use a network, we must be able to encode and interpret message, so that we can:
<ol start = "1">
	<li>Send a message to a specific location(by deciding which nodes to use or how to route them).</li>
	<li>Decide who can use the network and when they can use it, to avoid conflicting or faulty messages.</li>
</ol>
Ex. We can send a message using bits. These bits can be sent using electrons or photons. So we have:
<br>
<br>
<b>Message =&gt; bits =&gt; electrons/photons</b>
<br>
<br>
A router figures out which way to send the information. It will do it's best but can, of course, not be flawless. So in the case of our current internet, we have Best Effort Delivery with no guarantees of delivery time or bit-rate.
<br>
<br>
Read more about <a href = "https://en.wikipedia.org/wiki/Best-effort_delivery">Best Effort on Wikipedia</a>."""],
				['lesson-XIV-ii', 'Measuring a Network', """There are different ways of measuring a network. Either by time or by information-load.
<br>
<div class="part-concept">	
	<div class="part-concept-title">
		Latency
	</div>
	<div class="concept-description">
		The time that it takes for a message to go from source to destination. From the time when you start sending to the time when the receiver starts receiving.
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		Bandwidth
	</div>
	<div class="concept-description">
		The amount of information that can be transmitted by unit of time. Often measured in Mbps (Mega bits per second).
		<br>
		<br>
		A bit is the smallest unit of information. A binary choice of yes/no or 0/1. One bit can therefore allow us to choose between two different pieces of information.
		<br>
		<br>
		We can try to optimize our use of bits by creating questions that have a 50/50 chance of being yes or no.
		<br>
		<br>
		Also see <a href="https://en.wikipedia.org/wiki/Binary_tree">Binary Trees.</a>
	</div>
</div>"""],
				['lesson-XIV-iii', 'Protocols', """A protocol is a set of rules that define how a client(web browser) and a server communicate. Most web-sites use HTTP.
<br>
<br>
HTTP: <span class = "specialfont-1">H</span>yper <span class = "specialfont-1">T</span>ext <span class = "specialfont-1">T</span>ransfer <span class = "specialfont-1">P</span>rotocol
<br>
<br>
When a browser contacts a server, the chain of events can be described in the following way:
<ol start = "1">
	<li>Client sends a GET request to the server</li>
	<li>The server finds the requested object.</li>
	<li>The server sends back a response, consisting of the contents of the requested object.</li>
</ol>"""]
			],

			[
				'Important Terminology',
				['lesson-XV-i', 'Web Communication', """Some of the following has been covered before and thus appears earlier in the notes. But I have chosen to write them down, so that I can refer back to them when reviewing this stage.
<div class="part-concept">	
	<div class="part-concept-title">
		HTML document layout
	</div>
	<div class="concept-description">
		&lt;!DOCTYPE HTML&gt;: the type of document, i.e. HTML5
		<br>
		<br>
		&lt;html&gt; and &lt;/html&gt; are the opening and closing tags around the entire document, minus the doctype.
		<br>
		<br>
		&lt;head&gt; and &lt;/head&gt; are the opening and closing tags for the head, which can contain meta-data, Javascript, CSS and the document title, which appears in the top of a browser tab. Written in the following way:  &lt;title&gt;&quot;Name of the page&quot;&lt;/title&gt;
		<br>
		<br>
		Then we have the body tag, which is the actual content of the document/site. &lt;body&gt; and &lt;/body&gt; open and close this part of the document.
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		URL: Uniform Resource Locator
	</div>
	<div class="concept-description">
		This is written in the following way:
		<br>
		<br>
		http://www.nameofsite.com/
		<br>
		<br>
		The <b>http</b> is the <span class="specialfont-2">protocol</span>, followed by a colon and two slashes.
		<br>
		Then we have the <span class="specialfont-2">host</span> (in this example <b>www.nameofsite.com</b>), followed by a slash, which leads us to the <span class = "specialfont-2">path</span>. 
		<br>
		<br>
		The host is translated into an IP address. More reading on IP on wikipedia here: <a href = "https://en.wikipedia.org/wiki/Internet_Protocol">Internet Protocol</a>
		<br>
		<br>
		The path can be any number of sub-paths, like sub-domains, single pages etc.
	</div>
</div><div class="part-concept">	
	<div class="part-concept-title">
		Query parameters (or GET parameters)
	</div>
	<div class="concept-description">
		An example is:
		<br>
		<br>
		http://example.com/foo?p=1&amp;q=neat
		<br>
		<br>
		The query parameter is basically a name that is assigned a value, so in this case the first name is p with the value 1 and the second name is q with the value neat.
	</div>
</div><div class="part-concept">	
	<div class="part-concept-title">
		Fragment
	</div>
	<div class="concept-description">
		An example is:
		<br>
		<br>
		http://example.com/foo#fragment
		<br>
		<br>
		The fragment is not sent as a request to the server but exists purely in the browser.
		If the fragment follows a query parameter, it follows that query parameter.
	</div>
</div><div class="part-concept">	
	<div class="part-concept-title">
		The port
	</div>
	<div class="concept-description">
		In the following URL:
		<br>
		<br>
		http://localhost:8000/
		<br>
		<br>
		localhost is the address of the machine we are working on and :8000 is the port. The default value for the port is :80.
		<br>
		<br>
		This is important if you are a web-developer, as it is very likely that you will be accessing your machine through some port, often not the default port 80.
	</div>
</div><div class="part-concept">	
	<div class="part-concept-title">
		HTTP
	</div>
	<div class="concept-description">
		HTTP, as has been mentioned several times, stands for Hyper Text Transfer Protocol
		<br>
		<br>
		This is the protocol that a browser uses when talking to web-servers
		<br>
		<br>
		The browser can send a request for the URL www.example.com/foo. 
		The request begins with a request line.
		<br>
		<br>
		An example is:
		<br>
		GET /foo HTTP/1.1
		<br>
		<br>
		The request line consists of three parts. The method (GET), the path (/foo) and the version(HTTP 1.1)
		<br>
		<br>
		Requests are followed by headers, using the format <span class="specialfont-3">name: value</span>
		<br>
		<br>
		Headers can be:
		<br>
		Host: www.example.com
		<br>
		User-agent: chrome v.17
		<br>
		<br>
		You can create any header you want to add meta-info to a request
	</div>
</div><div class="part-concept">	
	<div class="part-concept-title">
		HTTP response
	</div>
	<div class="concept-description">
		These are simple responses and may look like: HTTP/1.1 200 OK. This is the status line
		<br>
		<br>
		In this we have the HTTP version (HTTP 1.1), the status code (200) and the reason phrase (OK)
		<br>
		<br>
		The status code tells us whether things work or whether there's an error, like the infamous 404 error that everyone has probably encountered.
		Here's a useful wikipedia list of HTTP responses: <a href = "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes">HTTP responses</a>
		<br>
		<br>
		The response is also followed by headers, such as:
		<br>
		<br>
		Date:
		<br> 
		Server: 
		<br>
		Content-type:
		<br>
		Content-length: 
	</div>
</div><div class="part-concept">	
	<div class="part-concept-title">
		Servers
	</div>
	<div class="concept-description">
		Servers respond to HTTP requests as mentioned earlier.
		<br>
		<br>
		We can differentiate between <span class="specialfont-2">static</span> and <span class="specialfont-2">dynamic</span> content.
		<br>
		Basically static content consists of pre-written files and images.
		<br>
		<br>
		Dynamic content is what we refer to as web-applications, and allow users to add or change what they are seeing, by making changes on the fly. Like Facebook, where you can add pictures, write stuff etc.
	</div>
</div>"""]
			],

			[
				'Forms',
				['lesson-XVI-i', 'Forms', """A form is a part of an HTML document which let's a user input data, like text, the click of a virtual button etc.
<br>
<br>
For this, we use the &lt;form&gt; tag
<br>
<br>
The form tag can contain different tags, like for example the &lt;input&gt; tag, which allows us to take in input.
<br>
<br>
<b>The input can have different attributes like:</b>
<div class="part-concept">	
	<div class="part-concept-title">
		name
	</div>
	<div class="concept-description">
		example:
		<br>
		<br>
		&lt;input name = &quot;the_name_of_the_input_value&quot;&gt;
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		type
	</div>
	<div class="concept-description">
		example:
		<br>
		<br>
		&lt;input type = &quot;submit&quot;&gt;
		<br>
		&lt;input type = &quot;text&quot;&gt;
		<br>
		&lt;input type = &quot;password&quot;&gt;
		<br>
		&lt;input type = &quot;checkbox&quot;&gt;
		<br>
		&lt;input type = &quot;radio&quot;&gt;
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		value
	</div>
	<div class="concept-description">
		example:
		<br>
		<br>
		&lt;input type = &quot;radio&quot; value = &quot;something&quot;&gt;
	</div>
</div>
Forms have different attributes like:
<div class="part-concept">	
	<div class="part-concept-title">
		action
	</div>
	<div class="concept-description">
		example:
		<br>
		<br>
		&lt;form action = &quot;/foo&quot;&gt;
		<br>
		<br>
		This tells the browser where the form should submit the input to, in this case it is the path /foo of the web-page the form is a part of.
		<br>
		<br>
		Using the example:
		<br>
		<br>
		&lt;form action = &quot;http://www.google.com/search&quot;&gt;
		<br>
		<br>
		we can perform a google search from our input box.
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		label
	</div>
	<div class="concept-description">
		example:
		<br>
		<br>
		&lt;label&gt;
		<br>
		&nbsp;&nbsp;&nbsp;&nbsp;One
		<br>
		&nbsp;&nbsp;&nbsp;&nbsp;&lt;input type = &quot;radio&quot; name = &quot;q&quot; value = &quot;one&quot;&gt;
		<br>
		&lt;/label&gt;
		<br>
		<br>
		This labels the radio-button with the text One
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		select
	</div>
	<div class="concept-description">
		example:
		<br>
		<br>
		&lt;select name = &quot;q&quot;&gt;
		<br>
		&nbsp;&nbsp;&nbsp;&nbsp;&lt;option&gt;One&lt;/option&gt;
		<br>
		&nbsp;&nbsp;&nbsp;&nbsp;&lt;option&gt;Two&lt;/option&gt;
		<br>
		&nbsp;&nbsp;&nbsp;&nbsp;&lt;option&gt;Three&lt;/option&gt;
		<br>
		&lt;/select&gt;
		<br>
		<br>
		This creates a dropdown menu with the options One, Two and Three, where we can select either of these three for our value of q.
		<br>
		<br>
		If we give one of the options a value, for example value = &quot;1&quot;, this assigns the value 1 to q when the action is performed, as opposed to just giving it the value that the option states, i.e. One.
	</div>
</div>"""]
			],

			[
				'Modulus and Dictionaries',
				['lesson-XVII-i', 'Modulus Operator', """This is an operator that gives us the remainder of a division operation between two numbers. It is written with the <span class="specialfont-2">%</span>, i.e.
<br>
<br>
&lt;number&gt;%&lt;modulus&gt;.
<br>
<br>
In the example: <b>15%18</b>, we get 3, since this is the remainder when dividing 15 by 18."""],
				['lesson-XVII-ii', 'Dictionary', """Dictionaries are similar to strings and lists, in that they contain a sequence of something. But where the string is a sequence of characters (perhaps creating a word or sentence) and the list is a sequence of strings and/or integers, a dictionary is a sequence of pairs, each pair consisting of a key and a value. A dictionary is opened and closed with curly brackets {}.
<br>
<br>
Example (These are the name and ages of myself, my girlfriend and our son):
<br>
<br>
d = {'Jens': 38, 'Mette': 36, 'Nor': 2}
<br>
<br>
The values can be anything you want, even other dictionaries.
<br>
<br>
Where strings are immutable, dictionaries, like lists, are mutable.
When mutating a dictionary, we are actually updating that dictionary, in that we change the value for a key into something new like:
<br>
<br>
d[1] = 37, if Mette has just had a birthday and her aged needs updating.
<br>
<br>
When indexing a string, we can get the nth character of a string by typing s[n] for the string s.
<br>
<br>
When indexing a list, we can get the nth element of a list by typing p[n] for the list p.
<br>
<br>
When indexing a dictionary, we can get the value of the nth key by typing d[n] for the dictionary d. Note that this only returns the value of the nth key, not the string or name of the value.
<br>
<br>"""]
			],

			[
				'Google App Engine',
				['lesson-XVIII-i', 'Some Basic info on GAE Datastore', """Tables are know as entities in GAED.
<ul>
<li>Columns are not fixed in GAED entities.</li>
<li>Every entity has an ID.</li>
<li>parents/ancestors, where an entity can be the child (or descendent) of another entity. The parent entity is referred to as an ancestor of the child.</li>
</ul>
When using the Datastore, it is important to read the documentation to understand what can be created and used. This also goes for pretty much anything in programming.
<br>
<br>
GAE is a convenient way of creating a small database. We are using Jinja2, which is built into GAE.
<br>
<br>
In Google App Engine, the default is HTML text, meaning that, unless told otherwise, the browser will interpret whatever you send as HTML.
<br>
If you want to be able to see the text, as read by humans, we can set the Content-Type to 'text/plain'.
<br>
<br>
Here's a link to <a href ="https://cloud.google.com/appengine/docs">Google App Engine</a> """],
				['lesson-XVIII-ii', 'GET vs POST', """I've gathered some info about GET and POSTS in the following table, for future reference.
<table>
	<tr>
		<td><b>GET</b></td>
		<td><b>POST</b></td>
	</tr>
	<tr>
		<td>Parameters in URL</td>
		<td>Parameters in body</td>
	</tr>
	<tr>
		<td>Used for fetching documents</td>
		<td>Used for updating data</td>
	</tr>
	<tr>
		<td>Have a maximum URL length</td>
		<td>Have no maximum length, but can be configured to have a max length</td>
	</tr>
	<tr>
		<td>OK to cache</td>
		<td>NOT OK to cache</td>
	</tr>
	<tr>
		<td>Shouldn't change the server, even though the same request repeats</td>
		<td>OK to change the server</td>
	</tr>
	<tr>
		<td>Conclusion!: Used mainly for fetching documents and data</td>
		<td>Conclusion!: Used mainly for updating server data</td>
	</tr>
</table>"""]
			],

			[
				'Validation',
				['lesson-XIX-i', 'Validation', """In short, validation means that your code (Server-side, which goes without saying) checks any inputs given to make sure that they are of the type that are expected.
<br>
<br>
Your server can receive junk, so it is important to be able to validate your parameters, so that your server knows what to expect and when to ignore or block invalid data(which could be harmful or just take up unnecessary space and memory)  from entering the system.
<br>
<br>
There are many ways of doing this. One way is to limit what the user can enter, by only giving them valid possibilities. But this is not a fool-proof method, so we have to (or should) do more than this.
<br>
<br>
But we also have to verify what the user enters and complain if the data is bad. You could, for example, create an error message will tell your user that you don't like their data or the way it is formatted.
<br>
<br>
I found an old article from 2002, by Paul Evans, which gives some good examples of validation and is both fun and informative to read: <a href="http://www.tldp.org/LDP/LG/issue83/evans.html">Validation</a>"""],
				['lesson-XIX-ii', 'String Substitution', """String substitution is great for returning different sets of text with different content, by having the possibility of exchanging certain words for others. Useful for when generating HTML that has to be able to change depending on (for example) user input.
<br>
<br>
For example, if we want to output some bold text, we can do it in the following way:
<br>
<br>
&lt;b&gt;some bold text&lt;/b&gt;
<br>
<br>
But what if we want to be able to write any text and output it in bold letters without creating a new bold string every time? We can do the following:
<br>
<br>
a = &quot;some bold text&quot;
&quot;&lt;b&gt;%s&lt;/b&gt;&quot; %a
<br>
<br>
This also outputs the text <b>some bold text</b> in bold letters.
<br>
<br>
We can substitute several strings by writing %s1 and %s2, where s1 and s2 are two different variable strings that can be substituted."""],
				['lesson-XIX-iii', 'Value Attribute', """The value attribute allows us to give an input field/box a predefined value. This can be a specific word (or other type of value), as in the example, where the value is set to &quot;cool&quot;: 
<br>
<br>
&lt;input type = &quot;text&quot; value = &quot;cool&quot;&gt;
<br>
<br>
Or we can use string substitution, to make sure that the value is whatever the user has given us as input, as in:
<br>
<br>
&lt;input type = &quot;text&quot; value = &quot;%(users_input)s&quot;&gt;
<br>
<br>"""],
				['lesson-XIX-iv', 'Escaping', """If not written properly, your code can let a user input code through a form that may do more or less harmful things to it. They could, for example, add long pieces of code that ultimately could completely alter the way your website looks and behaves.
<br>
<br>
This can, however, be avoided by <span class = "specialfont-2">escaping</span> your code, whereby it is interpreted in it's raw form and will be displayed as such, without the formatting having any effect on your code. In the example of a comment to a blog, containing HTML formatting, the whole thing will be displayed as a string, with the HTML formatting being visible to the reader, in much the same way as if it had been coded to show formatting using things like &amp;lt; to display &lt;.
<br>
<br>
Substituting potentially harmful HTML tags, quotes and &amp; can be done using the built in cgi in Python, where we have the built in function cgi.escape, which will of course only work if we import cgi into our py file.
<br>
We can also use <span class = "orange_text">autoescape</span> = <span class = "purple_text">true</span> in our Jinja2 environment."""],
				['lesson-XIX-v', 'Redirection', """We use redirection to make our web-site with a form, blog or other thing become useable as more than a one-time thing that goes away every time we refresh the browser.
<br>
<br>
By redirecting to a new page, to deliver a message of succes or error, or to let us see the comment we just wrote, we get a more interactive page, that can develop over time with user input. If we didn't redirect, but just showed the results of, for example, a comment directly after input, we would just have a pretty useless form that has no long term use.
<br>
<br>"""],
				['lesson-XIX-vi', 'Communicating with the User', """When validating form input, it is important to communicate with the user, telling them if you are missing some information or if a field has been filled out incorrectly or seems to have the wrong type of formatting. This could be an e-mail address without an @, a phone number with unexpected characters in it or a message saying that a field is empty even though it should have content.
<br>
<br>
You can do this in many ways, for example by redirecting to an error page or by highlighting the incorrectly filled out field and telling them what you expect there.
<br>
<br>
There are many good articles on this topic, for example at <a href = "http://webdesign.tutsplus.com/articles/">tutsplus</a>
<br>
<br>
In addition to error messages, it can also be nice to tell the users when they have filled out your form correctly and to thank them for their contribution, signup or whatever it is they have done."""]
			],

			[
				'HTML Templates',
				['lesson-XX-i', 'The Basics of HTML Templates', """When writing HTML for a web application, templates are a great tool, enabling us to write shorter and better code that can be reused to create the style and general content of several pages or bits of pages, in much the same way that CSS can be reused for styling the actual content of the HTML.
<br>
<br>
This let's us avoid unnecessary repetition, since we can code one or more templates that define the general look and usability of large parts of a website with many pages. We can, for example, create a template that gives us a header, a footer, menus and background for a page. This template can then be used for any and all pages where we want these things to be visible and usable. So not only do we only have to code it once, but we only store one version of this and only have to change this one template to make visible changes all across our site.
<br>
We do this by letting pages on our site inherit from a parent template in the way described a little further down the page.
<br>
<br>
Templates:
<br>
<ul>
	<li>Separate different types of code</li>
	<li>Make more readable code</li>
	<li>Make more secure websites</li>
	<li>Create HTML that is easier to modify</li>
	<li>Let us avoid repetition by reusing the same code for different sections of a site</li>
</ul>
<br>
<br>
A template library is a library that can help us build complicated strings(html).
<br>
<br>
For these lessons, we have used jinja2, which is built into Google App Engine. Read more about jinja2 at: <a href="http://www.jinja.pocoo.org
">jinja</a>
<br>
<br>
Below are some valuable things that can be used within HTML templates for making them versatile  and, as stated above, easily reused with different content.
<div class="part-concept">	
	<div class="part-concept-title">
		Variable Substitution
	</div>
	<div class="concept-description">
		When written within double curly brackets, the variable can be used many times and will, of course, change with the value of the variable in question:
		<br>
		<br>
		{{variable}}
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		Statement Syntax
	</div>
	<div class="concept-description">
		Statement syntax is written within curly brackets with percent signs. They allow us to use python loops (if, for etc.) and other similar things within our HTML.
		This is another place where we can avoid repetition in our code, as we can let a loop repeat itself a desired number of times,
		creating HTML code for each iteration. This is what I have done when creating all the sections for these notes.:
		<br>
		<br>
		{% statement %}
		<br>
		&nbsp;&nbsp;&nbsp;&nbsp;output
		<br>
		{% end statement %}
		<br>
		<br>
		example:
		<br>
		<br>
		{% if name == "Jens" %}
		<br>
		&nbsp;&nbsp;&nbsp;&nbsp;Hello Jens
		<br>
		{% else %}
		<br>
		&nbsp;&nbsp;&nbsp;&nbsp;Who might you be?
		<br>
		{% endif %}
		<br>
		<br>
		The final {% endif %} is there to tell jinja that the statement is ended and is there as a substitution for the whitespace we would use in python.
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		Helpful Tips
	</div>
	<div class="concept-description">
	writing a pipe and the word escape, will escape HTML syntax. like:
	<br>
	<br>
	| escape
	<br>
	<br>
	But better than the above is the aforementioned autoescape = True
	<br>
	<br>
	By writing a pipe and the word safe, we opt for unsafe mode, letting the input HTML code be active. Like:
	<br>
	<br>
	| safe
	<br>
	<br>
	Always automatically escape variables when possible!
	<br>
	<br>
	Minimize code in templates, where possible!
	<br>
	<br>
	Minimize html in your python code by keeping it in your templates!
	</div>
</div>
<div class="part-concept">	
	<div class="part-concept-title">
		Template inheritance
	</div>
	<div class="concept-description">
		You can make templates inherit from parent templates, by creating a basic template that contains everything that you want the user to see on every page that is a child of the template. The basic template has to contain the following in it's body:
		<br>
		<br>
		{% block content %}
		<br>
		This is where the content of the child goes.
		<br>
		{% endblock %}
		<br>
		<br>
		A child of this template starts with:
		<br>
		<br>
		{% extends "name_of_basic_template.html" %}
		<br>
		{% block content %}
		<br>
		this is where the child template's code goes
		<br>
		{% endblock  %}
	</div>
</div>"""]
			],

			[
				'Datastore',
				['lesson-XXI-i', 'Basic Database 101', """Any time you want to store large amounts of data, you will probably want to use a database. Some information on databases follows below.
				<div class="part-concept">	
					<div class="part-concept-title">
						What is a database
					</div>
					<div class="concept-description">
						<br>
						<br>
						A program that stores and retrieves large amounts of (structured) data.
						<br>
						<br>
						The word database can refer to:
						<br>
						<ul>
							<li>the program or database itself</li>
							<li>a machine (server) where the data(base) is stored</li>
							<li>several linked machines, where data is stored</li>
						</ul>
					</div>
				</div>
				<div class="part-concept">	
					<div class="part-concept-title">
						Table-structure in a database
					</div>
					<div class="concept-description">
						A database is often structured as a series of tables.
						<br>
						A series of columns gives us the standard types of data in each instance of data in the table. The instances are represented by the rows, each of which has one of each of the column types. These can be things  like ID, date, user, etc.
						<br>
						<br>
						Example table:
						<table>
							<tr>
								<td>ID</td>
								<td>USER</td>
								<td>DATE</td>
								<td>PASSWORD</td>
								<td>ANIMAL</td>
							</tr>
							<tr>
								<td>4</td>
								<td>geneatic53</td>
								<td>010100</td>
								<td>XXXXXXXXX</td>
								<td>goat</td>
							</tr>
							<tr>
								<td>7</td>
								<td>oprah45</td>
								<td>140672</td>
								<td>YYYYYYYYY</td>
								<td>gnu</td>
							</tr>
						</table>
						<br>
						<br>
						Now we can imagine if we had millions of table rows and had to write code to query this. There are numerous downsides of querying data by hand in this way, for example:
						<ul>
							<li>error-prone</li>
							<li>tedious</li>
							<li>slow</li>
						</ul>
						We want a databases to be able to take vast amounts of data and answer queries on them within a reasonable time.
						Luckily there are built-in wyas of doing this in most types of databases. One way of doing this is through indexes. See more further down the page.
					</div>
				</div>
				<div class="part-concept">	
					<div class="part-concept-title">
						Types of databases
					</div>
					<div class="concept-description">
						There are different types of databases. Here are some of them.
						One type of database is a so called Relational Database, using SQL(Structured Query Language). Read more about SQL on wikipedia <a href = "https://en.wikipedia.org/wiki/SQL">here</a>. The most popular relational databases are:
						<ul>
							<li>Postyresql</li>
							<li>MySQL</li>
							<li>SQLite</li>
							<li>Oracle(who also owns MySQL)</li>
						</ul>
						MySQL is used by almost everyone.
						<br>
						<br>
						SQLite is not as powerful, but sufficient for smaller projects like the one we are working on in the IPND.
						<br>
						<br>
						Other popular databases are:
						<ul>
							<li>Google AppEngine's Datastore</li>
							<li>Amazon Dynamo</li>
							<li>NoSQL databases like Mongo, or Couch</li>
						</ul>
					</div>
				</div>"""],
				['lesson-XXI-ii', 'SQL or Structured Query Language', """SQL was invented in the 1970's, long before the internet as we know it existed. It is not quite a programming language, but rather a language that is designed to query and get data from a database.
				<br>
				Below is an example of a SQL query. 
				<br>
				<br>
				SELECT * FROM links WHERE id = 5;
				<br>
				<br>
				Which basically means:
				<br>
				<ul>
					<li>SELECT == fetch data</li>
					<li>* == all columns</li>
					<li> FROM links == from a table with the name <i>links</i>table</li>
					<li> "id = 5" == a specific constraint</li>
				</ul>
				The constraint can use AND, OR, >, < etc. to create greater specificity
				<br>
				<br>
				We can also use ORDER BY to get our queries in a specific order, for example by date. We can control this by specifying Asc(ending) or Desc(ending), but the default is ascending."""],
				['lesson-XXI-iii', 'Joins', """As this is not something we have been using in this course, and I have been led to understand that it is not used very often, I'll just touch on this shortly.
				<br>
				<br>
				Joins are used to link several tables in a database, by some index that they may have in common. An example could be the you have a table with all user-data. In this table a user may have an ID. In another table, we may have a bunch of links or other input from users. One of the ways these can be sorted is by user ID. So this parameter can be used to link our two tables and to query data from one table through the other."""],
				['lesson-XXI-iv', 'Indexes', """When sequential scans are too slow, because of too many objects in a list/table/database, we can use indexing to sort the list that can be scanned easily, whereby we can increase our lookup time dramatically.
				<br>
				<br>
				For this we create a hashtable, like a library, where each indexed item has a key. These keys are not sorted and can be looked up just using the key. This gives us a constant lookup time which is not a function of the number of keys in the hashtable
				<br>
				<br>
				We can, however, use a tree instead of a hashtable. The tree is a sorted datastructure, where entities(the term used in GAE) can be parents or children of other entitites. Lookup time decreases with the size of the tree, but we get a nice and strict hierarchy."""],
				['lesson-XXI-v', 'ACID', """This is an abbreviation for a set of properties that ensure reliability in  database processing.
				<br>
				<br>
				<span class = "specialfont-1">A</span>tomicity: all parts of a transaction succeed or fail together.
				<br>
				<span class = "specialfont-1">C</span>onsistency: the database will always be consistent
				<br>
				<span class = "specialfont-1">I</span>solation: no transaction can interfere with another's, so each transaction has to (in some way) wait for another, even if they are input simultaneously
				<br>
				<span class = "specialfont-1">D</span>urability: once a transaction is committed, it won't be lost
				<br>
				<br>
				For a more in-depth description on the different factors, take a look at Wikipedias page on <a href="https://en.wikipedia.org/wiki/ACID">ACID</a>"""]
			],

			[
				'Meet Javascript',
				['lesson-XXII-i', 'Very Short Introduction', """
				JavaScript or JS is perhaps the most important programming language on the internet.
				 The reason for this is that JS is what we use to make pages more interesting by animating them.
				  This could be by adding moving elements that the user can control,
				   drop-down menus and any number of reactions to user-input.
				   <br>
				   <br>
				   JS can also be used to store simple data in variables and JSONs.
				"""],
				['lesson-XXII-ii', 'Truthy and Falsy', """
				In JS, we need to be able to use the Boolean values of True and False, but since all values aren't necessarily 100% true
				 or false, we have to define what evaluates to True and what evaluates to False. We call them Truthy and Falsy:
				 <br>
				 <table>
					<tr>
						<td><b>TRUTHY</b></td>
						<td><b>FALSY</b></td>
					</tr>
					<tr>
						<td>true</td>
						<td>false</td>
					</tr>
					<tr>
						<td>Non-zero numbers</td>
						<td>0</td>
					</tr>
					<tr>
						<td>&quot;strings&quot;</td>
						<td>&quot;&quot;</td>
					</tr>
					<tr>
						<td>objects</td>
						<td>undefined</td>
					</tr>
					<tr>
						<td>arrays</td>
						<td>null</td>
					</tr>
					<tr>
						<td>functions</td>
						<td>NaN (Not a Number)</td>
					</tr>
				</table>
				"""],
				['lesson-XXII-iii', 'Objects in JS', """
				Objects in JS are defined in ways different from the ways that classes and objects are defined in Python.
				<br>
				The thing is that THERE ARE NO CLASSES IN JS. JUST OBJECTS.
				<div class="part-concept">	
					<div class="part-concept-title">
						var
					</div>
					<div class="concept-description">
						Declaring a variable in Javascript is very similar to the way we do it in Python. The main difference is that JS uses the keyword var. For example:
						<br>
						<br>
						<span class="orange_text">var</span> <span class="purple_text">name</span> = &quot;PeterPiper&quot;; 
						<br>
						<br>
						You end a line in JS with a semicolon.
					</div>
				</div>
				<br>
				We can see that JS objects are quite similar to Python dictionaries. For example, I could create an object called Jens like this:
				<br>
				<br>
				<span class="orange_text">var</span> <span class="purple_text">Jens</span> = {<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&quot;name&quot; : &quot;Jens&quot;,<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&quot;surname&quot;: &quot;B&auml;ckvall&quot;,<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&quot;age&quot;: 39,<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&quot;City_of_Birth&quot;: &quot;Copenhagen&quot;<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&quot;contacts&quot;: {<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;email&quot;: &quot;jensbackvall@t-nova.org&quot;<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;phone&quot;: &quot;004525486484&quot;<br>
				&nbsp;&nbsp;&nbsp;&nbsp;}<br>
				}
				<br>
				<br>
				<div class="part-concept">	
					<div class="part-concept-title">
						Dot Notation and Bracket Notation for objects
					</div>
					<div class="concept-description">
						If I want to add new info to the Jens object, I can do it through dot notation. When adding the email, I could do it like this:
						<br>
						<br>
						Jens.email = &quot;jensbackvall@t-nova.org&quot;
						<br>
						<br>
						When using Dot Notation, we don't need to write var first, since we are adding properties to an excisting object, as opposed to creating a new object.
						<br>
						<br>
						We can do the same thing with Bracket Notation. It works like this:
						<br>
						<br>
						Jens[&quot;email&quot;] = &quot;jensbackvall@t-nova.org&quot;
					</div>
				</div>
				<div class="part-concept">	
					<div class="part-concept-title">
						Arrays
					</div>
					<div class="concept-description">
						Arrays in JS are pretty much like lists in Python. They contain a number of indexes, starting with the first one at index 0 and continuing up from there.
						<br>
						<br>
						Arrays, strings etc can be manipulated in many ways. I won't give any examples, but the link we were given to the Mozilla Developer's Network is a great place to explore:
						<a href= "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects">MDN on Global Objects</a>
					</div>
				</div>
				"""],
				['lesson-XXII-iv', 'JSON', """
				JavaScript Object Notation or JSON, is an easy to use format for storing data, nested or hierarchal. JSON allows for data to be encapsulated within other objects.
				<br>
				<br>
				Here is an example of a JSON, where a list(<b>array</b>) of motorless vehicles (named <b>no_motor</b>) are encapsulated within the overall object called <b>vehicles</b>:
				<br>
				<div class="part-concept">
				<span class="orange_text">var</span> <span class="purple_text">vehicles</span> = {<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&quot;no_motor&quot;: [<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;name&quot;: &quot;sailboat&quot;,<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;environment&quot;: &quot;water&quot;,<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;propulsion&quot;: &quot;wind&quot;<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;name&quot;: &quot;bicycle&quot;,<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;environment&quot;: &quot;land&quot;,<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&quot;propulsion&quot;: &quot;legs&quot;<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>
				&nbsp;&nbsp;&nbsp;&nbsp;]<br>
				}<br>
				</div>
				<br>
				Interesting reading on JSON here: <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON">MDN on JSON</a>
				<br>
				<br>
				It is important that JSON that is written by hand (as opposed to generated in other ways) be linted, meaning that it should be passed through a filter that looks for syntax errors, since these errors are very easy to make.<br>
				A good linter is <a href="http://www.jsonlint.com">jsonlint.com</a>
				"""]
			],

			[
				'The Power of APIs',
				['lesson-XXIII-i', 'Application Programming Interface', """
				APIs let your website or software communicate with other computers, components etc. An API has a set of functions or routines that can accomplish specific tasks within your software, giving output, taking input and generally interacting with whatever it is designed to interact with.
				<br>
				<br>
				Examples can be:
				<br>
				<br>
				<ul>
					<li>Accessing maps through your website and updating them through user interaction.</li>
					<li>Being able to send or receive SMS from a computer program. This could be for sending a mass-SMS to 100 (or many more) users at a time for some reason or other.</li>
					<li>Letting your program use specific hardware (speakers, camera etc) on the device upon which it is being run.</li>
					<li>Generally let your server communicate with other servers.</li>
					<li>Lots of other possibilities.</li>
				</ul>
				<br>
				I won't go deeper into APIs in these notes, as I have only worked with the examples given in the lesson.
				 But the concept is very interesting and I will certainly be delving deeper into using APIs in different ways 
				 in the future.
				 <br>
				 One of my plans, includes using the Twilio API to send SMS to audience members participating in interactive 
				 performing arts, as this type of theatre is my main field of work and I feel that using modern technology is a must 
				 for the arts.
				"""],
				['lesson-XXIII-ii', 'Parsing', """
				When getting data or reading code from another server, it must be <i>parsed</i>.
				<br>
				<br>
				Parsing means to take a string of symbols and analyse their meaning, while conforming to some grammatic rules,
				for example the grammatic rules of the programming language that is being parsed.
				<div class="part-concept">
				The term <i>parsing</i> comes from the Latin <i>pars (orationis)</i>, meaning <b>part (of speech)</b>
				</div>
				When reading code, a server has to parse it, using a <b>parser</b>. A parser is, very shortly put,
				a software component that takes input data and builds a data structure (source: <a href="https://en.wikipedia.org/wiki/Parsing#Parser">Wikipedia</a>)
				"""],
				['lesson-XXIII-iii', 'XML', """	
				XML is similar to HTML, but more rigorous. In XML every tag must have an opening and a closing tag. No void tags.
				<br>
				<br>
				XML and HTML share a common ancestor in <a href="https://en.wikipedia.org/wiki/Standard_Generalized_Markup_Language">SGML(Standard General Markup Language)</a>.
				<br>
				<br>
				So HTML can be expressed in XML, but they aren't the same. You can also write your code in XHTML, which is a more rigorous version of HTML.
				<br>
				<br>
				Read more about XHTML on Wikipedia here: <a href="https://en.wikipedia.org/wiki/XHTML">XHTML</a>.
				"""],
				['lesson-XXIII-iv', 'Good Internet Citizenship', """
				<b>Use a good user-agent</b>. In other words, make sure that you have a header or other means of letting a
				 website know who you are and how to contact you. This might be necessary if you are pulling a lot
				  of data from a site and for some reason they need you to stop.
				<br>
				<br>
				<b>Rate-limit yourself</b>. In other words, if you are requesting a lot of data from somewhere, 
				make sure that your program does it at an acceptable pace, so that you don't over-work the server's 
				you are sending requests to. For example by using the time.sleep() function in Python.
				"""]
			],

			[
				'Recursion & Parallell Computing',
				['lesson-XXIV-i', 'Recursion', """
				Recursive programming is basically writing a procedure that calls itself until a base case is
				 reached. To use the wording from the lesson, a recursive definition has two parts:
				<br>
				<br>
				<ol style="1">
					<li>Base Case, a starting point<br>
					Not defined in terms of itself<br>
					This uses the smallest input, we already know the answer
					</li>
					<li>Recursive Case<br>
					Defined in terms of <i>smaller</i> version of itself</li>
				</ol>
				The quiz we had during the lesson, where we had to define a procedure that checked if a word
				 is a palindrome was a great example. This was where I really felt that I could start picturing
				  and thereby internalizing what a recursive procedure does.
				<br>
				<br>
				<div class="part-concept">
				<span class="orange_text">def</span> is_palindrome(s):<br>
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="purple_text">if</span> s == '':<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return True<br>
				&nbsp;&nbsp;&nbsp;&nbsp;<span class="purple_text">else</span>:<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="purple_text">if</span> s[0] == s[-1]:<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return is_palindrome(s[1: -1])<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="purple_text">else</span>:<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return False<br>
				</div>
				<br>
				In this case, s is the base case, where we know that there are no characters and so the word has
				 no length and can <i>be called</i> (but I wonder what a linguist would say?) a palindrome, since
				  no length is the same backwards and forwards.<br>
				In this case we return the Boolean value True to tell us that we do indeed have a palindrome.
				<br>
				<br>
				After the base case (if it is not true, because the word is longer than nothing), the recursion starts,
				 by asking if the first and last letters of the word are the same. If they are, these are trimmed off
				  the word and the procedure is run <i>inside itself</i> to check if the new, trimmed word has reached
				   the base case. If it has, we know that the word is a palindrome, if not, we once again check if the 
				   first and last letters are the same.
				<br>
				<br>
				The recursion stops if:
				<ol style="a">
					<li>we reach the base case and we get a True, the word being a palindrome.</li>
					<li>the first and last letters are not the same, whereupon we get the Boolean False and know that 
					the word is not a palindrome.</li>
				</ol>
				"""],
				['lesson-XXIV-ii', 'Parallell Computing', """
				The very short introduction we were given to parallel computing tells us that this basically works by
				 splitting a large data collection into smaller chunks of data that are sorted, computed, stored etc. 
				 separately and at the same time. Then these smaller chunks of (now analysed in some way) data are 
				 brought together again. This is a much more efficient way of doing things when processing very large
				  amounts of data.
				<br>
				<br>
				<img src="https://computing.llnl.gov/tutorials/parallel_comp/images/parallelProblem.gif" class="img-responsive" 
				alt="parallell computing image from computing.llnl.gov">
				image from computing.llnl.gov
				<br>
				<br>
				Here is a nice introduction to parallel computing from <a href="https://computing.llnl.gov/tutorials/parallel_comp/#Whatis">computing.llnl.gov</a>.
				"""]
			],

			[
				'Solving Big Problems',
				['lesson-XXV-i', 'Solving Big Problems', """
				There are quite a lot of things to think about when starting to tackle a big problem. I've tried to gather the most important things I've taken away from this lesson in the following:
				<br>
				<div class="part-concept">	
					<div class="part-concept-title">
						Plan ahead
					</div>
					<div class="concept-description">
						When trying to solve a big coding problem, it is important to have a sense of <i>pacing</i>, to make sure that you don't get discouraged by trying to solve everything at once. For example:
						<br>
						<br>
						<ol style="1">
							<li>What are the components of the problem?</li>
							<li>Break the big problem into these components.</li>
							<li>Set yourself intermediate goals containing smaller parts of the whole problem.</li>
							<li>Go to each small part of the whole as a task in itself, disconnected from the whole, so that it becomes more manageable.</li>
						</ol>
					</div>
				</div>
				<div class="part-concept">	
					<div class="part-concept-title">
						As written in the instructor notes
					</div>
					<div class="concept-description">
						I liked this more in depth version of the short 4 point list I have written above, so I have copied it directly.
						<br>
						<br>
						From the big picture point of view, here is what Peter has done so far:
						<ul>
							<li>He took time to really understand what the problem is and broke it into smaller pieces.</li>
							<li>He went through each piece to see if it felt like something he could solve.</li>
							<li>He convinced himself that since each of those pieces are things he thinks he could solve, 
							he will be able to solve the entire problem.</li>
							<li>He acknowledged the size of the problem and mentally prepared himself.</li>
							<li>He wrote a function to solve one piece of the problem.</li>
							<li>He used that function and was unhappy with the results.</li>
							<li>He wrote tests for the function so he would know if future changes caused any problems.</li>
						</ul>
					</div>
				</div>
				<div class="part-concept">	
					<div class="part-concept-title">
						Regression test
					</div>
					<div class="concept-description">
						Create several possible solutions to a single problem, so that these solutions can be used later, 
						to check if they still work and how much time is used. This ensures that you don't make the code 
						worse, by making it slower or by changing it so that it suddenly does not find all possible solutions.
					</div>
				</div>
				<div class="part-concept">	
					<div class="part-concept-title">
						Initial simplification of a problem
					</div>
					<div class="concept-description">
						When solving problems, try to create a solution that is the most simple one. Even if this means 
						breaking some rules or parameters initally. Once you have a solution that works for the simplest 
						possible case, you can always start refining it so that more and more rules and/or parameters are 
						taken into account.
					</div>
				</div>
				And finally. Go one step at a time and don't get discouraged! Follow the steps above and remember to not 
				jump ahead to the next one until you're convinced that you've solved everything up to your current standing. 
				It is tempting to run ahead, but you might get lost if you do.
				"""]
			],

			[
				'My Choice of Final Project: Responsive Web Design & Bootstrap',
				['lesson-XXVI-i', 'Responsive Web Design', """After trying the courses at <a href="https://dash.generalassemb.
				ly/projects">Dash</a> and doing the <a href="https://www.udacity.com/course/viewer#!/c-ud304/l-2617868617/m-2698138588">
				Intro to HTML and CSS</a> course at Udacity, I decided that I'd like to know more about responsive web-design and Bootstrap
				 as these seemed very useful.
				<br>
				<br>
				<span class="specialfont-1">R</span>esponsive <span class="specialfont-1">W</span>eb <span class="specialfont-1">
				D</span>esign (or <span class="specialfont-1">RWD</span>) is simply the practice of making sure that the site you are
				 designing can be viewed and used on all (or most) devices, regardless of screen-size and orientation (meaning whether
				  you are holding your tablet/phone in portrait or landscape mode), and whether the input comes through a keyboard and
				   mouse(pad) or through a touch-screen.
				<br>
				The site should work without the user having to pan and scroll left and right a lot and any resizing of content should
				 not have to be done by the user, but should happen automatically.
				<br>
				<br>
				This image (which I am guessing more people than me have been using in their submissions :-P, since it is readily available
				 on Wikipedia and tells it like it is) shows the basic principle of RWD:
				<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Content-is-like-water-1980.jpg/1200px-Content-is-like-water-1980.jpg" class="img-responsive" alt="Water confirms to the vessel and so should your web-content">
				<br>
				<br>
				Some of the main things to think about when working with RWD are:
				<div class="part-concept">	
					Creating a fluid grid, where all elements on a page resize according to relative units, like a percentage of the page width or height.
				</div>
				<div class="part-concept">	
					Making sure that your images are also responsive, so that they resize along with the page elements they are placed within.
					 If this is not done, the images can stop the elements from resizing.
				</div>
				<div class="part-concept">	
					Making sure that Text sizes change with the size of the screen, so that words aren't chopped up if, for example, a heading becomes
					 much too large for a small phone screen.
				</div>
				<div class="part-concept">	
					Using Media Queries, where different CSS rules apply according to the width, height and orientation of the screen.
					<br>
					An example of a media query I wrote for one of my own web-sites:
					<br>
					<br>
					@media only screen and (max-device-width: 768px) and (orientation: portrait) {<br>
					&nbsp;&nbsp;&nbsp;&nbsp;body {<br>
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;background-image: url(&quot;IMAGES/Background-small-portrait.png&quot;);<br>
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;font-size: 27px;<br>
					&nbsp;&nbsp;&nbsp;&nbsp;}<br>
					&nbsp;&nbsp;&nbsp;&nbsp;div.text-box-38 {<br>
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;width: 48%;<br>
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;height: 1000px;<br>
					&nbsp;&nbsp;&nbsp;&nbsp;}<br>
					&nbsp;&nbsp;&nbsp;&nbsp;div.text-box-img-left {<br>
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;width: 48%;<br>
					&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;height: 1000px;<br>
					&nbsp;&nbsp;&nbsp;&nbsp;}<br>
					}
					<br>
					<br>
					In the above, I tell the CSS to use this for any device with a screen-width smaller than or equal to 768px when in portrait mode.
					 If this occurs, the background image will be different than it is for bigger screens or for the same screen in landscape mode.
					  The size of the font and the two main elements on the page also changes.
				</div>
				<br>
				The page I am refering to in the short section about media query can be found here:
				 <a href="http://www.kapow.humanimal.fitness">kapow.humanimal.fitness</a>
				<br>
				<br>
				It is basically just a responsive online flyer with just 4 pages in all. And it is in DANISH.
				 I've added the code to GITHUB so you can see it <a href="https://github.com/jensbackvall/Udacity-Nanodegree/tree/Stage-5---UPND/kapow">here</a>.
				"""],
				['lesson-XXVI-ii', 'Bootstrap', """
				Bootstrap is a, so called, Front-End Framework that can be used as basis for any website.
				 It contains pre-written CSS, JSS and lots of different elements that are ready to use in
				  your web-design.
				Started at Twitter, it is an open-source project.
				<br>
				<br>
				Currently at version 3(but they are advertising version 4 on their website), Bootstrap is now
				 written to work Mobile first, so that it is responsive from birth and helps the user create
				  scaleability for any device. There are exceptions where the user has to actively choose reponsive
				   images, make sure that drop-down (or drop-up) menus aren't obscured by the borders of the element
				    they era placed within etc.
				<br>
				<br>
				Examples of things that can be found and used in Bootstrap are:
				<ul>
					<li>a grid system for structuring the page</li>
					<li>drop-down menus</li>
					<li>buttons</li>
					<li>icons (called glyphicons)</li>
					<li>pop-up windows or modals</li>
					<li>carouselles for images</li>
					<li>collapsing elements</li>
					<li>and much more</li>
				</ul>
				<br>
				I would use examples of all of the above, but decided that it became quite messy,
				 so I trust that you trust that I have tried and understood them.
				 <br>
				 <br>
				 When using Bootstrap, it is not necessary to use normalize.css (see next section), as this is 
				 already included in Bootstrap, as we can see in the <a href="http://getbootstrap.com/css/#overview-normalize">documentation</a>.
				"""],
				['lesson-XXVI-iii', 'normalize.css', """
				Normalize.css is a css file that you can add to your website to make sure that it renders nicely and consistently. It is an add on to your own css and you should add it as the last css file in your html file, to make sure that it overrides any inconsistencies you may have inadvertently written.
				<br>
				<br>
				To quote what the creators Nicolas Gallagher and Jonathan Neal write about it:
				<br>
				<br>
				<b><i>&quot;Normalize.css makes browsers render all elements more consistently and in line with 
				modern standards. It precisely targets only the styles that nees normalizing.&quot;</i></b>
				<br>
				<br>
				you can find normalize.css here: <a href="https://necolas.github.io/normalize.css/">normalize</a>
				"""],
				['lesson-XXVI-iv', 'This IPND Notes Site', """
				When creating this, newest, version of my IPND notes page, I decided to use Bootstrap and only retain some of my old CSS in a new CSS file. This has become my <i>final project</i> for this nanodegree, although I would have liked to delve deeper into some other subjects, more specifically Front-End, Full-Stack and iOS Developer. But that will have to wait for later, as I didn't have the time to do multiple things before the deadline.
				<br>
				<br>
				I used the Bootstrap grid system to create the basis of the page and then saved the new page as the index.html file that I use with my main.py file to run the site on Google AppEngine.
				<br>
				<br>
				I had to change some of the main.py, but not very much. The most important thing I did, was to not render several different pages, but stick to the index.html, where I used the CSS target selector to display any content within the same page element when the title is clicked in the table of contents.
				I also put all my variables with my page content into one single variable that I could easily loop through, making my html much shorter and better than it was previously.
				<br>
				<br>
				Bootstrap does a lot of stuff for you, but some things are not the way you want them, which is to be expected. If this wasn't the case, Bootstrap would either be a ridiculously intelligent mind-reading AI or we would all be very boring people who liked all websites to be virtually the same :-)
				<br>
				<br>
				So, I changed some of the CSS in the Bootstrap CSS file, so that I didn't have to override it with my own CSS. I did this mainly because I could and felt like it, even though leaving it alone and writing code in my own CSS file would have been cleaner and easier to back out off.
				The things I changed are basically the background colour of a menu element, the max-width of the same element and other small stuff like that. 
				But once that is said, I do have quite a bit of CSS left to control the looks of the page, and several bits of it are used to override the bootstrap.css.
				But all in all, I have far less css than I had for the original page that I submitted for 
				Stages 1-4.
				<br>
				<br>
				<b>An important note on font-size!</b> I decided to let the text in the header of the page 
				stay the same size, even though it creates a line-break when viewed on smaller devices. I think it looks nice 
				at that size and the line-break doesn't occur in a disturbing way. Just to make it clear that this was a choice and 
				not a moment of forgetfullness :-).
				<br>
				<br>
				I also added a little Javascript to make sure that the page loads on a welcome screen rather than on an empty element. This is at the bottom of the page and not in a .js file. I feel that this was the best choice, as this JS specifically targets the HTML elements above it and has to do with the showing of the page.
				<br>
				<br>
				The whole page is responsive, thanks to Bootstrap and the fact that I have made sure that all img elements use the img-responsive class, so that they don't stop the page from resizing. I have decided to leave the page as it is now, where it simply becomes a long column on narrower screens, since this works nicely for me and there will be some scrolling no matter what I do.
				<br>
				<br>
				And that is about all I have to say about the page as it is. Enjoy the resources in the final section.
				"""],
				['lesson-XXVI-v', 'Resources', """
				I have used many external resources during the course of this nanodegree, but the ones that have been the
				 most important for this final stage are the Documentation for Bootstrap and Stackoverflow.com. The first
				  being the one go-to I had for using Bootstrap and the second being the  place where I could find answers
				   to all of my questions, big and small, stupid and hopefully not-so-stupid.
				<br>
				<br>
				In addition to these, I really enjoyed the simple and clear lessons at Dash, where I learnt some quick and
				 easy tricks for simple, responsive web-design. Dash can hardly be deemed an additional link, as it was a
				  part of the course, but I'm adding it anyway, as it was not compulsory and I really did make use of it
				   for my deeper dive into RWD.
				<br>
				<br>
				<div class="part-concept">
					<div class="part-concept-title">
						Bootstrap Documentation
					</div>	
					<br>
					Link: <a href="http://getbootstrap.com/about/">http://getbootstrap.com/about/</a>
					<br>
					<br>
					The Bootstrap documentation gives the reader a good overview of how, when and where to use Bootstrap.
					It introduces all of the elements that can be used and that are included in Bootstrap and any rules
					 that you need to know to use these elements properly. All of this is presented in an easily searchable
					   page with clear titles in the menus.<br>
					The documentation has individual pages for CSS, JS and other components, as well as a specific page for
					 customizing and downloading(entitled Customize)  a bootstrap.css file containing the elements that you
					  want to use when designing your page. This means that you don't have to download CSS and JS files
					   containing everything that Bootstrap can do, but can limit yourself to your own specifics.
					I like that fact that they have included visual examples of most of the things you can do with Bootstrap
					 along with notes on how to use them and, in many cases, how to go around possible problems.
				</div>
				<div class="part-concept">
					<div class="part-concept-title">
						Stackoverflow.com
					</div>	
					<br>
					Link: <a href="http://stackoverflow.com/tour">http://stackoverflow.com/tour</a>
					<br>
					<br>
					Stackoverflow is, simply put, a Q&A site for programmers, where anyone can create a profile and start
					 posting their questions on programming.<br>
					One of the great things about stackoverflow is that there is room for everyone, from super-newbs to
					 the most advanced programmers who might have questions that are way beyond anything that I have even
					  heard of. And they all help to answer each other's questions!<br>
					When searching for something related to programming or wondering about an unknown error-message,
					 chances are that you'll get search hits leading you straight to a relevant question and answer on stackoverflow,
					  often complete with examples or links to examples.<br>
					Stackoverflow has a few, strict and important rules to make sure that no unwanted content enters the site.
					 Among these is the first and most important rule:
					<br>
					<br>
					&quot;<i>Don't ask about questions you haven't tried to find an answer for(show your work!)</i>&quot;
					<br>
					<br>
					In other words, you are required to add some code or an explanation for why you are asking the question. This is great for several reasons.
					<ol style="a">
						<li>It is easier for others to benefit from your question, and for you to benefit from other's questions.</li>
						<li>It is easier for people to answer, or attempt to answer, your question.</li>
					</ol>
					I urge anyone who is coding, at any level, to use stackoverflow for any and all problems code-related. It's a true open-source library of knowledge.
					<br>
					<br>
					Here's a link to a question that I have posted: <a href="http://stackoverflow.com/questions/34558065/python-in-html-iterating-over-several-lists-by-changing-the-name-of-a-variable?">My First Stackoverflow Question</a>
				</div>
				<div class="part-concept">
					<div class="part-concept-title">
						Dash
					</div>	
					<br>
					Link: <a href="https://dash.generalassemb.ly/">https://dash.generalassemb.ly/</a>
					<br>
					<br>
					Dash is a tutorial web-site, that quickly and easily takes you through simple web-programming skills,
					 like basic HTML, CSS and JS.<br>
					In their 5 short projects, they touch upon many important subjects and hold your hand all the way
					 through, without guiding you so much that you don't learn anything.<br><br>
					Dash will not, on it's own, make you an expert Front-End designer, but it shows you how easy it can be
					 and makes it fun by breaking the tutorials up into little bits, where you are congratulated for every
					  small step you take.<br>
					All in all, Dash is a great introduction to web-programming for anyone who wants to give it a go before
					 enrolling in more time-consuming education.
				</div>
				"""]
			]
		]
