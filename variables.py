lesson1 = [
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
				<p class="p-center">
					<img src="http://imbreannarose.com/wp-content/uploads/2012/10/html-lessons-img-tag.jpg" alt="this should be a neat img poster">
				</p>			"""],
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
				]

lesson2 = [
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
				]

lesson3 = [
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
				When I wrote the code for this page, I started by creating all the containers or &lt;div&gt;s for everything for every element on the page, like <span class="specialfont-3">Lesson1</span>, <span class="specialfont-3">Lesson2</span> and <span class="specialfont-3">Lesson3</span>, with different parts, like <span class="specialfont-3">The Web</span>, <span class="specialfont-3">Online Resources</span> or <span class="specialfont-3">CSS</span> nested inside them.
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
				]

#lesson4 = [
				# ['a', 'b', """c"""],
				# ['a', 'b', """c"""],
				# ['a', 'b', """c"""]
				# ]
