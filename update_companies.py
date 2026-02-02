#!/usr/bin/env python3
"""
Script to generate the complete companies data structure with website and careers URLs
"""

# Generate the JavaScript object with all companies
print("""
// Company data - paste this into app.html
const companies = {
    'FAANG & Big Tech': {
        icon: '🧠',
        companies: [
            { name: 'Meta (Facebook)', website: 'https://www.meta.com', careers: 'https://www.metacareers.com' },
            { name: 'Amazon', website: 'https://www.amazon.com', careers: 'https://www.amazon.jobs' },
            { name: 'Apple', website: 'https://www.apple.com', careers: 'https://www.apple.com/careers' },
            { name: 'Netflix', website: 'https://www.netflix.com', careers: 'https://jobs.netflix.com' },
            { name: 'Google', website: 'https://www.google.com', careers: 'https://careers.google.com' },
            { name: 'Microsoft', website: 'https://www.microsoft.com', careers: 'https://careers.microsoft.com' },
            { name: 'Adobe', website: 'https://www.adobe.com', careers: 'https://adobe.wd5.myworkdayjobs.com/AdobeCareers' },
            { name: 'Salesforce', website: 'https://www.salesforce.com', careers: 'https://www.salesforce.com/company/careers' },
            { name: 'Oracle', website: 'https://www.oracle.com', careers: 'https://www.oracle.com/corporate/careers' },
            { name: 'IBM', website: 'https://www.ibm.com', careers: 'https://www.ibm.com/employment' }
        ]
    },
    'Web3 / Crypto Infrastructure': {
        icon: '🪙',
        companies: [
            { name: 'OpenSea', website: 'https://opensea.io', careers: 'https://opensea.notion.site/OpenSea-Careers-94ba94c930d3452990d25112f7f4038a' },
            { name: 'Coinbase', website: 'https://www.coinbase.com', careers: 'https://www.coinbase.com/careers' },
            { name: 'Kraken', website: 'https://www.kraken.com', careers: 'https://www.kraken.com/careers' },
            { name: 'Binance', website: 'https://www.binance.com', careers: 'https://careers.binance.com' },
            { name: 'Gemini', website: 'https://www.gemini.com', careers: 'https://www.gemini.com/careers' },
            { name: 'Bitfinex', website: 'https://www.bitfinex.com', careers: 'https://www.bitfinex.com/careers' },
            { name: 'Bitstamp', website: 'https://www.bitstamp.net', careers: 'https://www.bitstamp.net/careers' },
            { name: 'OKX', website: 'https://www.okx.com', careers: 'https://www.okx.com/us/careers' },
            { name: 'Blockchain.com', website: 'https://www.blockchain.com', careers: 'https://www.blockchain.com/careers' },
            { name: 'MoonPay', website: 'https://www.moonpay.com', careers: 'https://moonpay.com/careers' },
            { name: 'Alchemy', website: 'https://www.alchemy.com', careers: 'https://www.alchemy.com/careers' },
            { name: 'Chainalysis', website: 'https://www.chainalysis.com', careers: 'https://www.chainalysis.com/careers' },
            { name: 'TRM Labs', website: 'https://www.trmlabs.com', careers: 'https://www.trmlabs.com/careers' },
            { name: 'Fireblocks', website: 'https://www.fireblocks.com', careers: 'https://www.fireblocks.com/careers' },
            { name: 'Anchorage Digital', website: 'https://www.anchorage.com', careers: 'https://www.anchorage.com/careers' },
            { name: 'Blockdaemon', website: 'https://blockdaemon.com', careers: 'https://blockdaemon.com/careers' },
            { name: 'Infura', website: 'https://infura.io', careers: 'https://infura.io/careers' },
            { name: 'Consensys', website: 'https://consensys.net', careers: 'https://consensys.net/careers' },
            { name: 'Polygon', website: 'https://polygon.technology', careers: 'https://polygon.technology/careers' },
            { name: 'Solana Labs', website: 'https://solana.com', careers: 'https://solana.com/careers' },
            { name: 'Avalanche', website: 'https://www.avax.network', careers: 'https://www.avax.network/careers' },
            { name: 'Near Protocol', website: 'https://near.org', careers: 'https://near.org/careers' },
            { name: 'Arbitrum', website: 'https://arbitrum.io', careers: 'https://offchainlabs.com/careers' },
            { name: 'Optimism', website: 'https://optimism.io', careers: 'https://optimism.io/careers' },
            { name: 'The Graph', website: 'https://thegraph.com', careers: 'https://thegraph.com/careers' },
            { name: 'Aave', website: 'https://aave.com', careers: 'https://aave.com/careers' },
            { name: 'SushiSwap', website: 'https://sushi.com', careers: 'https://sushi.com/careers' },
            { name: 'Uniswap Labs', website: 'https://uniswap.org', careers: 'https://uniswap.org/careers' },
            { name: 'Pyth Network', website: 'https://pyth.network', careers: 'https://pyth.network/careers' },
            { name: 'Rarible', website: 'https://rarible.com', careers: 'https://rarible.com/careers' },
            { name: 'Magic Eden', website: 'https://magiceden.io', careers: 'https://magiceden.io/careers' },
            { name: 'LooksRare', website: 'https://looksrare.org', careers: 'https://looksrare.org/careers' },
            { name: 'Moonbeam', website: 'https://moonbeam.network', careers: 'https://moonbeam.network/careers' },
            { name: 'Moonwell', website: 'https://moonwell.xyz', careers: 'https://moonwell.xyz/jobs' },
            { name: 'MoonDAO', website: 'https://moondao.xyz', careers: 'https://moondao.xyz/careers' },
            { name: 'SideShift.ai', website: 'https://sideshift.ai', careers: 'https://sideshift.ai/jobs' },
            { name: 'BitGo', website: 'https://www.bitgo.com', careers: 'https://www.bitgo.com/careers' },
            { name: 'Ledger', website: 'https://www.ledger.com', careers: 'https://www.ledger.com/careers' },
            { name: 'Trezor', website: 'https://trezor.io', careers: 'https://trezor.io/careers' },
            { name: 'Balancer Labs', website: 'https://balancer.fi', careers: 'https://balancer.fi/careers' },
            { name: 'Compound Labs', website: 'https://compound.finance', careers: 'https://compound.finance/jobs' },
            { name: 'dYdX', website: 'https://dydx.exchange', careers: 'https://dydx.exchange/careers' },
            { name: 'Synthetix', website: 'https://synthetix.io', careers: 'https://synthetix.io/careers' },
            { name: 'Arweave', website: 'https://www.arweave.org', careers: 'https://www.arweave.org/jobs' },
            { name: 'Livepeer', website: 'https://livepeer.org', careers: 'https://livepeer.org/jobs' }
        ]
    },
    'Web3 Security / Audit': {
        icon: '🛠',
        companies: [
            { name: 'CertiK', website: 'https://www.certik.com', careers: 'https://jobs.lever.co/certik' },
            { name: 'OpenZeppelin', website: 'https://www.openzeppelin.com', careers: 'https://www.openzeppelin.com/careers' },
            { name: 'Code4rena', website: 'https://code4rena.com', careers: 'https://web3.career/web3-companies/code4rena' },
            { name: 'Sherlock', website: 'https://www.sherlock.xyz', careers: 'https://web3.career/web3-companies/sherlock' },
            { name: 'Halborn', website: 'https://www.halborn.com', careers: 'https://www.halborn.com/careers' },
            { name: 'Trail of Bits', website: 'https://www.trailofbits.com', careers: 'https://apply.workable.com/trailofbits' },
            { name: 'Quantstamp', website: 'https://quantstamp.com', careers: 'https://quantstamp.com/careers' },
            { name: 'Hacken', website: 'https://hacken.io', careers: 'https://hacken.io/careers' }
        ]
    },
    'Cloud & Developer Platforms': {
        icon: '☁️',
        companies: [
            { name: 'GitHub', website: 'https://github.com', careers: 'https://github.com/about/careers' },
            { name: 'GitLab', website: 'https://gitlab.com', careers: 'https://about.gitlab.com/jobs' },
            { name: 'Atlassian', website: 'https://www.atlassian.com', careers: 'https://www.atlassian.com/company/careers' },
            { name: 'Docker', website: 'https://www.docker.com', careers: 'https://www.docker.com/careers' },
            { name: 'HashiCorp', website: 'https://www.hashicorp.com', careers: 'https://www.hashicorp.com/careers' },
            { name: 'DigitalOcean', website: 'https://www.digitalocean.com', careers: 'https://www.digitalocean.com/careers' },
            { name: 'Netlify', website: 'https://www.netlify.com', careers: 'https://www.netlify.com/careers' },
            { name: 'Vercel', website: 'https://vercel.com', careers: 'https://vercel.com/careers' },
            { name: 'Render', website: 'https://render.com', careers: 'https://render.com/careers' },
            { name: 'Cloudflare', website: 'https://www.cloudflare.com', careers: 'https://www.cloudflare.com/careers' },
            { name: 'Fastly', website: 'https://www.fastly.com', careers: 'https://www.fastly.com/careers' },
            { name: 'PagerDuty', website: 'https://www.pagerduty.com', careers: 'https://www.pagerduty.com/careers' },
            { name: 'Elastic', website: 'https://www.elastic.co', careers: 'https://www.elastic.co/about/careers' },
            { name: 'New Relic', website: 'https://newrelic.com', careers: 'https://newrelic.com/about/careers' },
            { name: 'JetBrains', website: 'https://www.jetbrains.com', careers: 'https://www.jetbrains.com/company/careers' },
            { name: 'MongoDB', website: 'https://www.mongodb.com', careers: 'https://www.mongodb.com/careers' },
            { name: 'Redis Labs', website: 'https://redislabs.com', careers: 'https://redislabs.com/careers' },
            { name: 'Databricks', website: 'https://databricks.com', careers: 'https://databricks.com/company/careers' },
            { name: 'Confluent', website: 'https://www.confluent.io', careers: 'https://www.confluent.io/careers' }
        ]
    },
    'SaaS & Platform': {
        icon: '📊',
        companies: [
            { name: 'Slack', website: 'https://slack.com', careers: 'https://slack.com/careers' },
            { name: 'Zoom', website: 'https://www.zoom.us', careers: 'https://careers.zoom.us' },
            { name: 'Twilio', website: 'https://www.twilio.com', careers: 'https://www.twilio.com/company/jobs' },
            { name: 'Shopify', website: 'https://www.shopify.com', careers: 'https://www.shopify.com/careers' },
            { name: 'Stripe', website: 'https://stripe.com', careers: 'https://stripe.com/jobs' },
            { name: 'Square', website: 'https://squareup.com', careers: 'https://squareup.com/us/en/careers' },
            { name: 'PayPal', website: 'https://www.paypal.com', careers: 'https://www.paypal.com/careers' },
            { name: 'Intuit', website: 'https://www.intuit.com', careers: 'https://www.intuit.com/careers' },
            { name: 'Asana', website: 'https://asana.com', careers: 'https://asana.com/jobs' },
            { name: 'Notion', website: 'https://www.notion.so', careers: 'https://www.notion.so/careers' },
            { name: 'Figma', website: 'https://www.figma.com', careers: 'https://www.figma.com/careers' },
            { name: 'Miro', website: 'https://miro.com', careers: 'https://miro.com/careers' },
            { name: 'Canva', website: 'https://www.canva.com', careers: 'https://www.canva.com/careers' },
            { name: 'Airtable', website: 'https://www.airtable.com', careers: 'https://www.airtable.com/careers' },
            { name: 'ClickUp', website: 'https://clickup.com', careers: 'https://clickup.com/careers' },
            { name: 'Monday.com', website: 'https://monday.com', careers: 'https://monday.com/careers' },
            { name: 'Smartsheet', website: 'https://www.smartsheet.com', careers: 'https://www.smartsheet.com/careers' },
            { name: 'Zendesk', website: 'https://www.zendesk.com', careers: 'https://www.zendesk.com/jobs' },
            { name: 'Datadog', website: 'https://www.datadog.com', careers: 'https://www.datadog.com/careers' },
            { name: 'Snowflake', website: 'https://www.snowflake.com', careers: 'https://www.snowflake.com/careers' },
            { name: 'UiPath', website: 'https://www.uipath.com', careers: 'https://www.uipath.com/company/careers' },
            { name: 'Snyk', website: 'https://snyk.com', careers: 'https://snyk.com/careers' },
            { name: 'Zapier', website: 'https://zapier.com', careers: 'https://zapier.com/jobs' },
            { name: 'Intercom', website: 'https://www.intercom.com', careers: 'https://www.intercom.com/careers' },
            { name: 'HubSpot', website: 'https://www.hubspot.com', careers: 'https://www.hubspot.com/careers' },
            { name: 'Qualtrics', website: 'https://www.qualtrics.com', careers: 'https://www.qualtrics.com/careers' }
        ]
    },
    'AI / ML Companies': {
        icon: '🤖',
        companies: [
            { name: 'OpenAI', website: 'https://openai.com', careers: 'https://openai.com/careers' },
            { name: 'Anthropic', website: 'https://www.anthropic.com', careers: 'https://www.anthropic.com/careers' },
            { name: 'Stability AI', website: 'https://stability.ai', careers: 'https://stability.ai/about/careers' },
            { name: 'Hugging Face', website: 'https://huggingface.co', careers: 'https://huggingface.co/careers' },
            { name: 'Cohere', website: 'https://cohere.com', careers: 'https://txt.cohere.com/careers' },
            { name: 'Adept', website: 'https://www.adept.ai', careers: 'https://www.adept.ai/jobs' },
            { name: 'Jasper', website: 'https://www.jasper.ai', careers: 'https://www.jasper.ai/careers' },
            { name: 'Runway', website: 'https://runwayml.com', careers: 'https://runwayml.com/jobs' },
            { name: 'Replit', website: 'https://replit.com', careers: 'https://replit.com/jobs' },
            { name: 'DeepMind', website: 'https://deepmind.com', careers: 'https://deepmind.com/careers' },
            { name: 'AI21 Labs', website: 'https://www.ai21.com', careers: 'https://www.ai21.com/careers' },
            { name: 'Scale AI', website: 'https://scale.com', careers: 'https://scale.com/careers' }
        ]
    },
    'Fintech': {
        icon: '💳',
        companies: [
            { name: 'Plaid', website: 'https://plaid.com', careers: 'https://plaid.com/careers' },
            { name: 'Brex', website: 'https://www.brex.com', careers: 'https://www.brex.com/careers' },
            { name: 'Chime', website: 'https://www.chime.com', careers: 'https://www.chime.com/careers' },
            { name: 'Robinhood', website: 'https://robinhood.com', careers: 'https://robinhood.com/careers' },
            { name: 'SoFi', website: 'https://www.sofi.com', careers: 'https://www.sofi.com/careers' },
            { name: 'Affirm', website: 'https://www.affirm.com', careers: 'https://www.affirm.com/careers' },
            { name: 'Klarna', website: 'https://www.klarna.com', careers: 'https://www.klarna.com/careers' }
        ]
    }
};
""")

print("\n\n// Render function - paste this to replace the renderCompanies function\n")
print("""
function renderCompanies(searchTerm = '') {
    const container = document.getElementById('companiesContainer');
    const search = searchTerm.toLowerCase();
    
    let html = '';
    let totalCompanies = 0;
    
    Object.entries(companies).forEach(([category, data]) => {
        const filteredCompanies = data.companies.filter(company => 
            company.name.toLowerCase().includes(search)
        );
        
        if (filteredCompanies.length > 0) {
            totalCompanies += filteredCompanies.length;
            html += `
                <div class="company-category">
                    <h3 class="category-title">
                        <span class="category-icon">${data.icon}</span>
                        ${category} (${filteredCompanies.length})
                    </h3>
                    <div class="company-table">
                        <table>
                            <thead>
                                <tr>
                                    <th style="width: 40%">Company</th>
                                    <th style="width: 30%">Website</th>
                                    <th style="width: 30%">Careers</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${filteredCompanies.map(company => `
                                    <tr>
                                        <td class="company-name-cell">${company.name}</td>
                                        <td>
                                            <a href="${company.website}" target="_blank" class="company-link">
                                                <span class="link-icon">🌐</span> Visit Site
                                            </a>
                                        </td>
                                        <td>
                                            <a href="${company.careers}" target="_blank" class="company-link">
                                                <span class="link-icon">💼</span> Careers
                                            </a>
                                        </td>
                                    </tr>
                                `).join('')}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }
    });
    
    if (html) {
        container.innerHTML = html;
        // Update header with count
        document.querySelector('.companies-header h2').textContent = `${totalCompanies} Companies Directory`;
    } else {
        container.innerHTML = '<div class="empty-state"><div class="empty-state-icon">📭</div><h2>No companies found</h2></div>';
    }
}
""")
