Bluhm 2020 Hacktoberfest Event
==============================

This is our repository for the 2020 Hacktoberfest challenge. The goal for this
event is to get everyone familiar with Git and GitHub which are both extremely
useful tools in basically any digital asset based project.

Along with Git, we will be exploring specific interests expressed by members of
the "clan:"

- Aiden - Python (DnD Game)
- Alex - Jekyll
- Leah - Ruby, Markdown, RESTful APIs
- Laura - Python, APIs
- Dad - Ruby
- Jenae - Python(?)

## The Game Plan

In order to hit at least a little the different interests and get everyone to 4
substantial pull requests to this repository, we will work on and include the
following artifacts:

### Jekyll Site

The Jekyll Site combines 3 different interests: Jekyll, Ruby, and Markdown.

[Jekyll](https://jekyllrb.com/) is an extremely popular static site generator,
created by GitHub to integrate into their GitHub pages platform, written in Ruby
with content written as HTML or Markdown. Jekyll utilizes templates to generate
a site that is well-themed, has some dynamics to them through client-side
Javascript in the browser, and make writing things like blog articles easy.

Here is an example of what Jekyll pages look like:

```markdown
---
layout: post
title:  "Welcome to Jekyll!"
date:   2020-10-24 09:59:37 -0400
categories: jekyll update
---
You’ll find this post in your `_posts` directory. Go ahead and edit it and
re-build the site to see your changes. You can rebuild the site in many
different ways, but the most common way is to run `jekyll serve`, which launches
a web server and auto-regenerates your site when a file is updated.

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit
numbers, and `MARKUP` is the file extension representing the format used in the
file. After that, include the necessary front matter. Take a look at the source
for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most
out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub
repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll
Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
```

[Follow this tutorial for more info on Jekyll and using Jekyll.][1]

[1]: https://jekyllrb.com/docs/step-by-step/01-setup/

### Python Projects

The other artifact(s) of this repository will be a set of python projects.

These will be found in the `projects` directory and will have their own specific
documentation for running them within the project sub-folders.

## Useful tools and links

### Git tutorials

- [Git Immersion](https://gitimmersion.com/index.html) - Introduction to Git
  with some really helpful tips along the way that I still use every day. It
  uses Ruby as the language to play around with. An interesting tie in would be
  to create your own project folder under the `projects` directory and create
  pull requests for each lab to commit your progress to this repository.

- [Git Kraken - Git basics](https://www.gitkraken.com/resources/learn-git) - A
  series of videos on some of the basics of git and git repositories.

- [Your first pull request with Git Kraken walk through (WIP)](https://docs.google.com/presentation/d/1ZEe21EEcLlEFWcBiQErfgrKA-Ze0EYuLwqTAN6sXLnQ/edit?usp=sharing) - A mini tutorial that will walk you through your first PR.
