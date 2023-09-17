---
title: OpenTF forked Terraform is now available
published: false
description:
tags: terraform, opentf, iac
---

## Table of Contents

<ol>
  <li><a href="#introduction">Introduction</a></li>
  <li><a href="#target-audience">Target Audience</a></li>
  <li><a href="#about-open-source">About Open Source</a></li>
  <li><a href="#impact-of-hashicorps-license-change">Impact of HashiCorp's license change</a></li>
  <li><a href="#the-foundations-claims">The Foundation's claims</a></li>
</ol>

## Introduction

In August 2023, HashiCorp, a developer of OSS such as Terraform, switched Terraform from an open source license to the Business Source License (BSL).

https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license

This license change will not directly affect HashiCorp users of Terraform and other products. However, there is a movement against HashiCorp's license change, and a group has formed to pursue true open source, forked from Terraform. It is [OpenTF Foundation](https://opentf.org/).

According to the manifesto, the OpenTF Foundation had demanded that HashiCorp switch Terraform back to an open-source license in order for Terraform to remain truly open source, and stated that it would maintain OpenTF forked from Terraform, if HashiCorp would not.

And so, on September 6, 2023 OpenTF was forked.

![](/blog-posts/opentf-fork-available/assets/image1.png)  
*https://x.com/opentforg/status/1699076153968095494?s=20*

What kind of OSS is OpenTF? And why did they decide to fork from Terraform? Let's take a look at their manifesto.

## Target Audience

- People who want to know about OpenTF
- People who want to know about the Foundation's claims

## About Open Source

The term "truly open source" appears several times in the above manifesto.  
I wasn't sure what "truly open source" meant, so I checked the definition of open source. The Open Source Initiative (OSI)[^1] has the [following definition of open source](https://opensource.org/definition-annotated/).

1. Free Redistribution
2. Source Code
3. Derived Works
4. Integrity of The Author’s Source Code
5. No Discrimination Against Persons or Groups
6. No Discrimination Against Fields of Endeavor
7. Distribution of License
8. License Must Not Be Specific to a Product
9. License Must Not Restrict Other Software

[^1]: https://opensource.org/

## Impact of HashiCorp's license change

HashiCorp's newly adopted license, the Business Source License(BSL)[^2], allows the release of the source code, but restricts commercial use. Because it a restricted use license, the owner clearly states that the BSL is not an open source license.

> Q: Is the BSL an Open Source license?[^3]  
> A: The BSL does not meet the Open Source Definition (OSD) maintained by the Open Source Initiative (OSI). OSD does not allow limitations on specific kinds of such, such as production use. However, most of the OSD criteria are met. Most important, the source code is made available. The BSL allows for copying, modification, creation of derivative works, redistribution, and non-production use of the code. It allows for (and encourages) the licensor to define an Additional Use Grant (e.g., allowing for free use below a specified level, like in this example).

However, HashiCorp clearly states that it allows the commercial use, except for use such as incorporating Terraform into a competing company's product.

> All non-production uses are permitted. All production uses are allowed other than hosting or embedding the software in an offering competitive with HashiCorp commercial products, hosted or self-managed.[^4]

What does the term “embedded” mean under the HashiCorp BSL license? HashiCorp answered this question.

> Under the HashiCorp BSL license, the term “embedded” means including the source code or object code, including executable binaries, from a HashiCorp product in a competitive product. “Embedded” also means packaging the competitive product in such a way that the HashiCorp product must be accessed or downloaded for the competitive product to operate.

Don't get me wrong, even if we are building a competing product for HashiCorp, there is nothing wrong with using their Vault for the purpose of securing a product that competes with Terraform, or deploying in Terraform to build a product that competes with the Vault.[^5]

[^2]: https://mariadb.com/bsl11/
[^3]: https://mariadb.com/bsl-faq-adopting/#osl
[^4]: https://www.hashicorp.com/license-faq#who-is-impacted
[^5]: https://www.hashicorp.com/license-faq#competitive-product-bsl-coverage

## The Foundation's claims
