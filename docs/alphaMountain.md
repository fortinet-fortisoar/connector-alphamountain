
<h2>About the connector</h2>

<p>alphaMountain Threat Response integrates investigations informed by reputation scores of target hosts, domains, and IP addresses. It fetches indicators with risk scores and relevant content categorization.</p>

<p>This document provides information about the alphaMountain connector, which facilitates automated interactions, with a alphaMountain server using FortiSOAR&trade; playbooks. Add the alphaMountain connector as a step in FortiSOAR&trade; playbooks and perform automated operations with alphaMountain.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Authored By: Fortinet</p>

<p>Certified: No</p>

<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-alphamountain</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of alphaMountain server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the alphaMountain server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>alphaMountain</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the Rest API endpoint URL of the alphaMountain server to connect and perform automated operations.</td></tr>
<tr><td>API Key</td><td>Specify the API key to access the alphaMountain Rest API endpoint to which you will connect and perform the automated operations.</td></tr>
<tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified. <br/>By default, this option is selected, i.e., set to <code>true</code>.</td></tr>
</tbody></table>

<h2>Actions supported by the connector</h2>

<p>You can use the following automated operations in playbooks and also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Threat Score</td><td>Retrieve threat rating scores stored in the alphaMountain.ai cloud for the provided URL or URI</td><td>get_threat_score <br/>Investigation</td></tr>
<tr><td>Get URL Categories</td><td>Fetch categories associated with an internet URL using alphaMountain's statistical and neural network models, validated across multiple sources. Note Category IDs are returned for performance reasons instead of textual category strings.</td><td>get_url_categories <br/>Investigation</td></tr>
<tr><td>Get Likely Impersonated Domain for a URL</td><td>Identifies domains that a URI may impersonate, crucial for detecting phishing, cyber-squatting, and typo domains.</td><td>identify_impersonation_detection <br/>Investigation</td></tr>
<tr><td>Get Popularity of Domain</td><td>Retrieves the popularity ranking of a domain or hostname within the last 24 hours.</td><td>get_domain_popularity <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Get Threat Score</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Input Type</td><td>Select the input type to retrieve a single or multiple URL threat ratings stored in the alphaMountain.ai cloud<br><strong>If you choose 'Specific URL'</strong><ul><li>URL: Provide a specific URI or URL to retrieve threat ratings scores stored in the alphaMountain.ai cloud</li><li>Scan Depth: Select the scan depth to determine how thorough a real-time lookup should be performed. Each level may take more time to respond</li></ul><strong>If you choose 'Multiple URLs'</strong><ul><li>URLs: Specify the CSV list of URLs or URLs to retrieve threat ratings scores stored in the alphaMountain.ai cloud</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p>Output schema when you choose "Input Type" as "Specific URL":</p>

<pre>{
    "version": "",
    "status": {
        "threat": ""
    },
    "threat": {
        "score": "",
        "scope": "",
        "source": ""
    },
    "ttl": ""
}</pre>

<p>Output schema when you choose "Input Type" as "Multiple URLs":</p>

<pre>{
    "version": "",
    "status": {
        "threat/uris": ""
    },
    "scores": {}
}</pre>

<h3>operation: Get URL Categories</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Input Type</td><td>Select the input type to retrieve a single or multiple URL categories stored in the alphaMountain.ai cloud<br><strong>If you choose 'Specific URL'</strong><ul><li>URL: Provide a specific URI or URL to categorize using alphaMountain.ai cloud</li></ul><strong>If you choose 'Multiple URLs'</strong><ul><li>URLs: Specify the CSV list of URLs or URLs to categorize using alphaMountain.ai cloud</li></ul></td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<p>Output schema when you choose "Input Type" as "Specific URL":</p>

<pre>{
    "version": "",
    "status": {
        "category": ""
    },
    "category": {
        "categories": [],
        "scope": "",
        "confidence": ""
    },
    "ttl": ""
}</pre>

<p>Output schema when you choose "Input Type" as "Multiple URLs":</p>

<pre>{
    "version": "",
    "status": {
        "category/uris": ""
    },
    "categories": {}
}</pre>

<h3>operation: Get Likely Impersonated Domain for a URL</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>URL</td><td>Provide a URI or URL to identify impersonations detection</td></tr>
<tr><td>Limit</td><td>Provide a URI or URL to identify impersonations detection</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "version": "",
    "status": {
        "impersonate": ""
    },
    "impersonate": [],
    "ttl": ""
}</pre>

<h3>operation: Get Popularity of Domain</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Domain</td><td>Provide a fully qualified domain name to retrieve the popularity.</td></tr>
</tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "version": "",
    "status": {
        "popularity": ""
    },
    "popularity": {
        "popularity": ""
    },
    "ttl": ""
}</pre>

<h2>Included playbooks</h2>

<p>The <code>Sample - alphaMountain - 1.0.0</code> playbook collection comes bundled with the alphaMountain connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the <strong>Automation</strong> &gt; <strong>Playbooks</strong> section in FortiSOAR&trade; after importing the alphaMountain connector.</p>

<ul>
<li>Get Likely Impersonated Domain for a URL</li>
<li>Get Popularity of Domain</li>
<li>Get Threat Score</li>
<li>Get URL Categories</li>
</ul>

<p><strong>Note</strong>: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.</p>
