import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "portfoliodjango.settings")
django.setup()

from porfolio.models import Jobs, Tools, Usages, Projects

jobs = [
    {
        'id': "1",
        'logo': "./ethsign.png",
        'company': 'EthSign',
        'title': "Core Development Lead",
        'start_date': "2022-03-07",
        'end_date': "2023-09-15",
        'desc': "EthSign is an e-signing platform that utilizes blockchain technology to offer a decentralized, customizable and transparent version."
    },
    {
        'id': "2",
        'logo': "./prompti.png",
        'company': 'Prompti',
        'title': "Team Lead",
        'start_date': "2019-10-21",
        'end_date': "2022-02-25",
        'desc': "Prompti is a one-of-a-kind online marketplace where sponsors and talented individuals can negotiate and contract working relationships, where sponsors financially support prospects in exchange for participation in future income."
    },
    {
        'id': "3",
        'logo': "./evolent.png",
        'company': 'Evolent Health',
        'title': "Senior Application Developer",
        'start_date': "2015-11-02",
        'end_date': "2019-10-18",
        'desc': "Evolent Health is comprised of an experienced and committed group of health care professionals, unified by a passion for transforming the way care is delivered and experienced in the United States."
    },
    {
        'id': "4",
        'logo': "./koch.png",
        'company': 'Koch Industries Inc',
        'title': "Linux Software Engineer",
        'start_date': "2012-05-07",
        'end_date': "2015-10-09",
        'desc': "Koch Industries, Inc. is an American multinational conglomerate corporation based in Wichita, Kansas, and is the second-largest privately held company in the United States, after Cargill."
    }
]

# Insert data into the database
for job in jobs:
    Jobs.objects.create(
        logo=job['logo'],
        company=job['company'],
        title=job['title'],
        start_date=datetime.strptime(job['start_date'], '%Y-%m-%d').date(),
        end_date=datetime.strptime(job['end_date'], '%Y-%m-%d').date(),
        desc=job['desc']
    )
    
projects = [
    {
        'uid': 'token-table',
        'src': 'token-table.webp',
        'title': 'TokenTable',
        'desc': 'Elevate your fundraising, and token distribution with ease.',
        'url': 'https://www.tokentable.xyz/'
    },
    {
        'uid': 'ethsign',
        'src': 'ethsign.png',
        'title': 'EthSign',
        'desc': 'Secure document signing protocol anchored on Arweave',
        'url': 'https://www.ethsign.xyz/'
    },
    {
        'uid': 'currency-convertor',
        'src': 'currency-convertor.svg',
        'title': 'Currency Convertor',
        'desc': "The world's most trusted, fast and secure currency converter",
        'url': 'https://github.com/tenwiz/currency-convertor'
    },
    {
        'uid': 'github-battle',
        'src': 'github-battle.webp',
        'title': 'GitHub Battle',
        'desc': 'GitHub Popularity Battle with React and Firebase',
        'url': 'https://github.com/tenwiz/github2battle'
    },
    {
        'uid': 'winrealty',
        'src': 'winrealty.webp',
        'title': 'Winrealty',
        'desc': 'Real Estate listing web application',
        'url': 'https://www.thewinrealty.com/'
    }
]

# Insert data into the database
for project_data in projects:
    Projects.objects.create(
        uid=project_data['uid'],
        src=project_data['src'],
        title=project_data['title'],
        desc=project_data['desc'],
        url=project_data['url']
    )

usages = [
  "FrontEnd",
  "BackEnd",
  "Databases",
  "Testing",
  "Tools"
]

for usage in usages:
  Usages.objects.create(
    techTitle=usage
  )

tools = [
    {
        'url': './react.webp',
        'tool': 'React',
        'desc': 'UI Library',
        'href': 'https://react.dev',
        'usage_id': 1
    },
    {
        'url': './next.webp',
        'tool': 'Next.js',
        'desc': 'Popular open-source framework for building modern web applications using React',
        'href': 'https://nextjs.org',
        'usage_id': 1
    },
    {
        'url': './redux.webp',
        'tool': 'Redux',
        'desc': 'A Predictable State Container for JS Apps',
        'href': 'https://redux.js.org',
        'usage_id': 1
    },
    {
        'url': './tailwind.webp',
        'tool': 'Tailwind CSS',
        'desc': 'Utility-first CSS framework for rapidly building modern websites',
        'href': 'https://tailwindcss.com',
        'usage_id': 1
    },
    {
        'url': './ts.webp',
        'tool': 'TypeScript',
        'desc': 'Typed Superset of JavaScript Library',
        'href': 'https://www.typescriptlang.org',
        'usage_id': 1
    },
    {
        'url': './sass.webp',
        'tool': 'Sass',
        'desc': 'CSS Preprocessor',
        'href': 'https://sass-lang.com',
        'usage_id': 1
    },
    {
        'url': './vite.webp',
        'tool': 'VitePress',
        'desc': 'Static Site Generator',
        'href': 'https://vitepress.dev',
        'usage_id': 1
    },
    {
        'url': './node.webp',
        'tool': 'Node.js',
        'desc': "JavaScript runtime built on Chrome's V8 JavaScript engine",
        'href': 'https://nodejs.org/en',
        'usage_id': 2
    },
    {
        'url': './express.webp',
        'tool': 'Express',
        'desc': 'Node.js web application framework',
        'href': 'https://expressjs.com',
        'usage_id': 2
    },
    {
        'url': './nest.webp',
        'tool': 'Nest.js',
        'desc': 'A progressive Node.js framework',
        'href': 'https://nestjs.com',
        'usage_id': 2
    },
    {
        'url': './ruby.webp',
        'tool': 'Ruby on Rails',
        'desc': 'server-side web application framework written in Ruby',
        'href': 'https://rubyonrails.org/',
        'usage_id': 2
    },
    {
        'url': './postgre.webp',
        'tool': 'PostgreSQL',
        'desc': 'Relational Database, Object-Relational Database System',
        'href': 'https://www.postgresql.org',
        'usage_id': 3
    },
    {
        'url': './mongo.webp',
        'tool': 'MongoDB',
        'desc': 'NoSQL Database',
        'href': 'https://www.mongodb.com',
        'usage_id': 3
    },
    {
        'url': './mysql.webp',
        'tool': 'MySQL',
        'desc': 'Relational Database',
        'href': 'https://www.mysql.com/',
        'usage_id': 3
    },
    {
        'url': './amazon.webp',
        'tool': 'Amazon DynamoDB Database',
        'desc': 'Amazon Cloud Databases',
        'href': 'https://aws.amazon.com/pm/dynamodb/',
        'usage_id': 3
    },
    {
        'url': './orm.webp',
        'tool': 'TypeORM',
        'desc': 'ORM for TypeScript and JavaScript',
        'href': 'https://typeorm.io',
        'usage_id': 3
    },
    {
        'url': './mongoose.webp',
        'tool': 'Mongoose',
        'desc': 'MongoDB Object Modeling for Node.js',
        'href': 'https://mongoosejs.com',
        'usage_id': 3
    },
    {
        'url': './sequelize.webp',
        'tool': 'Sequelize',
        'desc': 'a modern TypeScript and Node.js ORM',
        'href': 'https://sequelize.org/',
        'usage_id': 3
    },
    {
        'url': 'jest.webp',
        'tool': 'Jest',
        'desc': 'Testing Framework',
        'href': 'https://jestjs.io/',
        'usage_id': 4
    },
    {
        'url': 'react-testing.webp',
        'tool': 'React Testing Library',
        'desc': 'Testing Library',
        'href': 'https://testing-library.com/docs/react-testing-library/intro/',
        'usage_id': 4
    },
    {
        'url': 'cypress.webp',
        'tool': 'Cypress',
        'desc': 'End-to-End Testing Framework',
        'href': 'https://www.cypress.io/',
        'usage_id': 4
    },
    {
        'url': 'supertest.webp',
        'tool': 'Supertest',
        'desc': 'Super-agent driven library',
        'href': 'https://github.com/ladjs/supertest',
        'usage_id': 4
    },
    {
        'url': 'sinon.webp',
        'tool': 'Sinon',
        'desc': 'Standalone test spies, stubs and mocks for JavaScript',
        'href': 'https://sinonjs.org/',
        'usage_id': 4
    },
    {
        'url': 'mocha.webp',
        'tool': 'Mocha',
        'desc': 'Feature-rich JavaScript test framework',
        'href': 'https://mochajs.org/',
        'usage_id': 4
    },
    {
        'url': 'chai.webp',
        'tool': 'Chai',
        'desc': 'BDD / TDD assertion library for node',
        'href': 'https://www.chaijs.com/',
        'usage_id': 4
    },
    {
        'url': 'rspec.webp',
        'tool': 'RSpec',
        'desc': 'Behaviour Driven Development for Ruby',
        'href': 'https://rspec.info/',
        'usage_id': 4
    },
    {
        'url': 'aws.webp',
        'tool': 'Amazon Web Services (AWS)',
        'desc': 'Cloud Computing Services',
        'href': 'https://aws.amazon.com/',
        'usage_id': 5
    },
    {
        'url': 'github.webp',
        'tool': 'GitHub Actions',
        'desc': 'CI/CD',
        'href': 'https://github.com/features/actions',
        'usage_id': 5
    },
    {
        'url': 'github.webp',
        'tool': 'GitHub',
        'desc': 'Version Control System',
        'href': 'https://github.com',
        'usage_id': 5
    },
    {
        'url': 'vercel.webp',
        'tool': 'Vercel',
        'desc': 'Hosting Platform',
        'href': 'https://vercel.com/',
        'usage_id': 5
    },
    {
        'url': 'vscode.webp',
        'tool': 'Visual Studio Code',
        'desc': 'Text Editor',
        'href': 'https://code.visualstudio.com/',
        'usage_id': 5
    },
    {
        'url': 'firefox.webp',
        'tool': 'Firefox',
        'desc': 'Web Browser',
        'href': 'https://www.mozilla.org/en-US/firefox/new/',
        'usage_id': 5
    },
    {
        'url': 'google.webp',
        'tool': 'Google Chrome',
        'desc': 'Web Browser',
        'href': 'https://www.google.com/chrome/',
        'usage_id': 5
    },
    {
        'url': 'figma.webp',
        'tool': 'Figma',
        'desc': 'Design Tool',
        'href': 'https://www.figma.com/',
        'usage_id': 5
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


