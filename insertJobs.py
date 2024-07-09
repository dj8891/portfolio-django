import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "portfoliodjango.settings")
django.setup()

from porfolio.models import Usages, Tools

job_instance = Tools.objects.all()
job_instance.delete()
# usages = [
#   "FrontEnd",
#   "BackEnd",
#   "Databases",
#   "Testing",
#   "Tools"
# ]

# for usage in usages:
#   Usages.objects.create(
#     techTitle=usage
#   )
tools = [
    {
        'url': './react.webp',
        'tool': 'React',
        'desc': 'UI Library',
        'href': 'https://react.dev',
        'usage_id': 26
    },
    {
        'url': './next.webp',
        'tool': 'Next.js',
        'desc': 'Popular open-source framework for building modern web applications using React',
        'href': 'https://nextjs.org',
        'usage_id': 26
    },
    {
        'url': './redux.webp',
        'tool': 'Redux',
        'desc': 'A Predictable State Container for JS Apps',
        'href': 'https://redux.js.org',
        'usage_id': 26
    },
    {
        'url': './tailwind.webp',
        'tool': 'Tailwind CSS',
        'desc': 'Utility-first CSS framework for rapidly building modern websites',
        'href': 'https://tailwindcss.com',
        'usage_id': 26
    },
    {
        'url': './ts.webp',
        'tool': 'TypeScript',
        'desc': 'Typed Superset of JavaScript Library',
        'href': 'https://www.typescriptlang.org',
        'usage_id': 26
    },
    {
        'url': './sass.webp',
        'tool': 'Sass',
        'desc': 'CSS Preprocessor',
        'href': 'https://sass-lang.com',
        'usage_id': 26
    },
    {
        'url': './vite.webp',
        'tool': 'VitePress',
        'desc': 'Static Site Generator',
        'href': 'https://vitepress.dev',
        'usage_id': 26
    },
    {
        'url': './node.webp',
        'tool': 'Node.js',
        'desc': "JavaScript runtime built on Chrome's V8 JavaScript engine",
        'href': 'https://nodejs.org/en',
        'usage_id': 27
    },
    {
        'url': './express.webp',
        'tool': 'Express',
        'desc': 'Node.js web application framework',
        'href': 'https://expressjs.com',
        'usage_id': 27
    },
    {
        'url': './nest.webp',
        'tool': 'Nest.js',
        'desc': 'A progressive Node.js framework',
        'href': 'https://nestjs.com',
        'usage_id': 27
    },
    {
        'url': './ruby.webp',
        'tool': 'Ruby on Rails',
        'desc': 'server-side web application framework written in Ruby',
        'href': 'https://rubyonrails.org/',
        'usage_id': 27
    },
    {
        'url': './postgre.webp',
        'tool': 'PostgreSQL',
        'desc': 'Relational Database, Object-Relational Database System',
        'href': 'https://www.postgresql.org',
        'usage_id': 28
    },
    {
        'url': './mongo.webp',
        'tool': 'MongoDB',
        'desc': 'NoSQL Database',
        'href': 'https://www.mongodb.com',
        'usage_id': 28
    },
    {
        'url': './mysql.webp',
        'tool': 'MySQL',
        'desc': 'Relational Database',
        'href': 'https://www.mysql.com/',
        'usage_id': 28
    },
    {
        'url': './amazon.webp',
        'tool': 'Amazon DynamoDB Database',
        'desc': 'Amazon Cloud Databases',
        'href': 'https://aws.amazon.com/pm/dynamodb/',
        'usage_id': 28
    },
    {
        'url': './orm.webp',
        'tool': 'TypeORM',
        'desc': 'ORM for TypeScript and JavaScript',
        'href': 'https://typeorm.io',
        'usage_id': 28
    },
    {
        'url': './mongoose.webp',
        'tool': 'Mongoose',
        'desc': 'MongoDB Object Modeling for Node.js',
        'href': 'https://mongoosejs.com',
        'usage_id': 28
    },
    {
        'url': './sequelize.webp',
        'tool': 'Sequelize',
        'desc': 'a modern TypeScript and Node.js ORM',
        'href': 'https://sequelize.org/',
        'usage_id': 28
    },
    {
        'url': 'jest.webp',
        'tool': 'Jest',
        'desc': 'Testing Framework',
        'href': 'https://jestjs.io/',
        'usage_id': 29
    },
    {
        'url': 'react-testing.webp',
        'tool': 'React Testing Library',
        'desc': 'Testing Library',
        'href': 'https://testing-library.com/docs/react-testing-library/intro/',
        'usage_id': 29
    },
    {
        'url': 'cypress.webp',
        'tool': 'Cypress',
        'desc': 'End-to-End Testing Framework',
        'href': 'https://www.cypress.io/',
        'usage_id': 29
    },
    {
        'url': 'supertest.webp',
        'tool': 'Supertest',
        'desc': 'Super-agent driven library',
        'href': 'https://github.com/ladjs/supertest',
        'usage_id': 29
    },
    {
        'url': 'sinon.webp',
        'tool': 'Sinon',
        'desc': 'Standalone test spies, stubs and mocks for JavaScript',
        'href': 'https://sinonjs.org/',
        'usage_id': 29
    },
    {
        'url': 'mocha.webp',
        'tool': 'Mocha',
        'desc': 'Feature-rich JavaScript test framework',
        'href': 'https://mochajs.org/',
        'usage_id': 29
    },
    {
        'url': 'chai.webp',
        'tool': 'Chai',
        'desc': 'BDD / TDD assertion library for node',
        'href': 'https://www.chaijs.com/',
        'usage_id': 29
    },
    {
        'url': 'rspec.webp',
        'tool': 'RSpec',
        'desc': 'Behaviour Driven Development for Ruby',
        'href': 'https://rspec.info/',
        'usage_id': 29
    },
    {
        'url': 'aws.webp',
        'tool': 'Amazon Web Services (AWS)',
        'desc': 'Cloud Computing Services',
        'href': 'https://aws.amazon.com/',
        'usage_id': 30
    },
    {
        'url': 'github.webp',
        'tool': 'GitHub Actions',
        'desc': 'CI/CD',
        'href': 'https://github.com/features/actions',
        'usage_id': 30
    },
    {
        'url': 'github.webp',
        'tool': 'GitHub',
        'desc': 'Version Control System',
        'href': 'https://github.com',
        'usage_id': 30
    },
    {
        'url': 'vercel.webp',
        'tool': 'Vercel',
        'desc': 'Hosting Platform',
        'href': 'https://vercel.com/',
        'usage_id': 30
    },
    {
        'url': 'vscode.webp',
        'tool': 'Visual Studio Code',
        'desc': 'Text Editor',
        'href': 'https://code.visualstudio.com/',
        'usage_id': 30
    },
    {
        'url': 'firefox.webp',
        'tool': 'Firefox',
        'desc': 'Web Browser',
        'href': 'https://www.mozilla.org/en-US/firefox/new/',
        'usage_id': 30
    },
    {
        'url': 'google.webp',
        'tool': 'Google Chrome',
        'desc': 'Web Browser',
        'href': 'https://www.google.com/chrome/',
        'usage_id': 30
    },
    {
        'url': 'figma.webp',
        'tool': 'Figma',
        'desc': 'Design Tool',
        'href': 'https://www.figma.com/',
        'usage_id': 30
    }
]
for tool_data in tools:
    Tools.objects.create(
        url=tool_data['url'],
        tool=tool_data['tool'],
        desc=tool_data['desc'],
        href=tool_data['href'],
        usage_id=Usages.objects.get(id=tool_data['usage_id'])
    )

