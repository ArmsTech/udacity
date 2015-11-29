"""Manage categories for tech_quote."""

PYTHON = {
    'category_id': 1, 'category_name': 'Python',
    'category_description': (
        'Python is a widely used general-purpose, high-level programming '
        'language. Its design philosophy emphasizes code readability, and its '
        'syntax allows programmers to express concepts in fewer lines of code '
        'than would be possible in languages such as C++ or Java. The '
        'language provides constructs intended to enable clear programs on '
        'both a small and large scale.'),
    'category_icon_url': 'https://www.python.org/static/img/python-logo.png'
}

JAVASCRIPT = {
    'category_id': 2, 'category_name': 'JavaScript',
    'category_description': (
        'JavaScript is a high-level, dynamic, untyped, and interpreted '
        'programming language. It has been standardized in the ECMAScript '
        'language specification. Alongside HTML and CSS, it is one of the '
        'three essential technologies of World Wide Web content production; '
        'the majority of websites employ it and it is supported by all modern '
        'web browsers without plug-ins.'),
    'category_icon_url': (
        'http://getmoai.com/images/icons/lang_icon_javascript.png')
}

JAVA = {
    'category_id': 3, 'category_name': 'Java',
    'category_description': (
        'Java is a general-purpose computer programming language that is '
        'concurrent, class-based, object-oriented, and specifically '
        'designed to have as few implementation dependencies as possible. It '
        'is intended to let application developers "write once, run anywhere" '
        '(WORA), meaning that compiled Java code can run on all platforms '
        'that support Java without the need for recompilation.'),
    'category_icon_url': (
        'https://upload.wikimedia.org/wikipedia/en/8/88/Java_logo.png')
}

CSHARP = {
    'category_id': 4, 'category_name': 'C#',
    'category_description': (
        'C# (pronounced as see sharp) is a multi-paradigm programming '
        'language encompassing strong typing, imperative, declarative, '
        'functional, generic, object-oriented (class-based), and '
        'component-oriented programming disciplines. It was developed by '
        'Microsoft within its .NET initiative and later approved as a '
        'standard by Ecma (ECMA-334) and ISO (ISO/IEC 23270:2006). C# is one '
        'of the programming languages designed for the Common Language '
        'Infrastructure.'),
    'category_icon_url': (
        'https://upload.wikimedia.org/wikipedia/commons/0/0d/C_Sharp_wordmark.svg')
}

C = {
    'category_id': 5, 'category_name': 'C',
    'category_description': (
        'C, (as in the letter c) is a general-purpose, imperative computer '
        'programming language, supporting structured programming, lexical '
        'variable scope and recursion, while a static type system prevents '
        'many unintended operations.'),
    'category_icon_url': (
        'https://upload.wikimedia.org/wikipedia/commons/3/35/The_C_Programming_Language_logo.svg')
}

RUBY = {
    'category_id': 6, 'category_name': 'Ruby',
    'category_description': (
        'Ruby is a dynamic, reflective, object-oriented, general-purpose '
        'programming language. It was designed and developed in the mid-1990s '
        'by Yukihiro "Matz" Matsumoto in Japan. It supports multiple '
        'programming paradigms, including functional, object-oriented, and '
        'imperative. It also has a dynamic type system and automatic memory '
        'management.'),
    'category_icon_url': (
        'https://upload.wikimedia.org/wikipedia/commons/7/73/Ruby_logo.svg')
}

CPLUS = {
    'category_id': 7, 'category_name': 'C++',
    'category_description': (
        'C++ (pronounced as cee plus plus) is a general-purpose programming '
        'language. It has imperative, object-oriented and generic '
        'programming features, while also providing facilities for low-level '
        'memory manipulation.'),
    'category_icon_url': (
        'http://www.technewsable.com/wp-content/uploads/2015/07/c-logo.png')
}

SWIFT = {
    'category_id': 8, 'category_name': 'Swift',
    'category_description': (
        'Swift is a multi-paradigm, compiled programming language created by '
        'Apple Inc. for iOS, OS X, watchOS and tvOS development. Swift is '
        'designed to work with Apple\'s Cocoa and Cocoa Touch frameworks and '
        'the large body of existing Objective-C code written for Apple '
        'products.'),
    'category_icon_url': (
        'https://upload.wikimedia.org/wikipedia/commons/9/9d/Swift_logo.svg')
}

R = {
    'category_id': 9, 'category_name': 'R',
    'category_description': (
        'R is a programming language and software environment for statistical '
        'computing and graphics supported by the R Foundation for Statistical '
        'Computing. The R language is widely used among statisticians and '
        'data miners for developing statistical software and data analysis.'),
    'category_icon_url': (
        'https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg')
}

SQL = {
    'category_id': 10, 'category_name': 'SQL',
    'category_description': (
        'SQL (Structured Query Language) is a special-purpose programming '
        'language designed for managing data held in a relational database '
        'management system (RDBMS), or for stream processing in a relational '
        'data stream management system (RDSMS).'),
    'category_icon_url': (
        'http://geeklad.com/wp-content/uploads/2012/02/sql.png')
}

ALL_CATEGORIES = [
    PYTHON, JAVASCRIPT, JAVA, CSHARP, C, RUBY, CPLUS, SWIFT, R, SQL]
