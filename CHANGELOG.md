# Changelog

## 0.19.0 (2026-04-18)

Full Changelog: [v0.18.1...v0.19.0](https://github.com/ArkHQ-io/ark-python/compare/v0.18.1...v0.19.0)

### Features

* **api:** add tenantId to send ([3eddd67](https://github.com/ArkHQ-io/ark-python/commit/3eddd677b69f387149336e11abe71a6143290ac4))
* **internal:** implement indices array format for query and form serialization ([6b0e47e](https://github.com/ArkHQ-io/ark-python/commit/6b0e47e19fdb9c5c52804bfe7f2a65e7dad7d9a9))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([8c48bf3](https://github.com/ArkHQ-io/ark-python/commit/8c48bf31ef7fdce13c5e23e23c144134b004ecb6))
* **deps:** bump minimum typing-extensions version ([f968d32](https://github.com/ArkHQ-io/ark-python/commit/f968d32304f3254d028211fd71f3cc4be8a9d61b))
* ensure file data are only sent as 1 parameter ([6c9b9b8](https://github.com/ArkHQ-io/ark-python/commit/6c9b9b804042c0472d0de84a1ee7241bb2b66f92))
* **pydantic:** do not pass `by_alias` unless set ([5c61281](https://github.com/ArkHQ-io/ark-python/commit/5c612819f12b4b87159d751625fc2e64d1e3dd1f))
* sanitize endpoint path params ([d4ca0b1](https://github.com/ArkHQ-io/ark-python/commit/d4ca0b1e86263ef3e7ededd8c9a88949dfc15e2e))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([56e6c32](https://github.com/ArkHQ-io/ark-python/commit/56e6c326d177ea84008c9622e2d835cdc669e8b3))


### Chores

* **ci:** bump uv version ([e7115ed](https://github.com/ArkHQ-io/ark-python/commit/e7115edad4dd96f45c7b87f76b00792b8d096647))
* **ci:** skip lint on metadata-only changes ([7a77a86](https://github.com/ArkHQ-io/ark-python/commit/7a77a86a2f0ff316277469d42e5185dd3f154dc9))
* **ci:** skip uploading artifacts on stainless-internal branches ([5ad9ccb](https://github.com/ArkHQ-io/ark-python/commit/5ad9ccb223dc029f721420b94bb87a7a7207bdb3))
* **internal:** add request options to SSE classes ([fdc5e91](https://github.com/ArkHQ-io/ark-python/commit/fdc5e91d4774006a051e8a289bbd1b3c7eec1b8c))
* **internal:** codegen related update ([a6cc237](https://github.com/ArkHQ-io/ark-python/commit/a6cc237ae03c83da16f8cc279dac4fe5e91e0816))
* **internal:** make `test_proxy_environment_variables` more resilient ([709aff4](https://github.com/ArkHQ-io/ark-python/commit/709aff401224092c3e5059559951c8bc82c59866))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([df5b863](https://github.com/ArkHQ-io/ark-python/commit/df5b8639e08e14c7a64e51081f60c41d0450617b))
* **internal:** tweak CI branches ([a50b7f8](https://github.com/ArkHQ-io/ark-python/commit/a50b7f8017b23cae995700f9a0a579bfc4b5a57b))
* **internal:** update gitignore ([f048789](https://github.com/ArkHQ-io/ark-python/commit/f04878939392dd78362c34806681a3d7082888ae))
* **test:** do not count install time for mock server timeout ([e9620f6](https://github.com/ArkHQ-io/ark-python/commit/e9620f619e9f8bafc0d3fdc2b070cb4e6f5454b3))
* **tests:** bump steady to v0.19.4 ([2f78979](https://github.com/ArkHQ-io/ark-python/commit/2f78979a8b73ee72108b8e514373d36a62aafc26))
* **tests:** bump steady to v0.19.5 ([41a53dc](https://github.com/ArkHQ-io/ark-python/commit/41a53dc50fca7e7e9a2928ad72d06ad2259837d3))
* **tests:** bump steady to v0.19.6 ([b952880](https://github.com/ArkHQ-io/ark-python/commit/b95288045bc908c0bb6a76addf6ac8d344f69ac3))
* **tests:** bump steady to v0.19.7 ([c07a4ff](https://github.com/ArkHQ-io/ark-python/commit/c07a4ffc2a582f51718e6f31e5908a1aa55d2d30))
* **tests:** bump steady to v0.20.1 ([ba432f3](https://github.com/ArkHQ-io/ark-python/commit/ba432f3f2ccbde4b5144f0836de29e957f6024b4))
* **tests:** bump steady to v0.20.2 ([0d2aa8d](https://github.com/ArkHQ-io/ark-python/commit/0d2aa8dc868885578f6a2e9e2423f3a0f2132134))
* **tests:** bump steady to v0.22.1 ([02c097b](https://github.com/ArkHQ-io/ark-python/commit/02c097b129dc7c64bb163a288789e75a95121c60))
* update mock server docs ([b4e4ce8](https://github.com/ArkHQ-io/ark-python/commit/b4e4ce8a56859a87137349e5f97ede2c8acaad25))


### Refactors

* **tests:** switch from prism to steady ([18f705f](https://github.com/ArkHQ-io/ark-python/commit/18f705f1fff9c42d14de17f0eb50eb1232ff9019))

## 0.18.1 (2026-02-18)

Full Changelog: [v0.18.0...v0.18.1](https://github.com/ArkHQ-io/ark-python/compare/v0.18.0...v0.18.1)

### Chores

* format all `api.md` files ([0bb7fa6](https://github.com/ArkHQ-io/ark-python/commit/0bb7fa631696cd81593b96fed2a10b0928fa96e5))
* **internal:** bump dependencies ([63156f5](https://github.com/ArkHQ-io/ark-python/commit/63156f537a5cd335171716189b8c2b485186b3ea))
* **internal:** fix lint error on Python 3.14 ([8ed190d](https://github.com/ArkHQ-io/ark-python/commit/8ed190d76e8eee53ab12dde18e07b007eed57dbc))

## 0.18.0 (2026-02-05)

Full Changelog: [v0.17.0...v0.18.0](https://github.com/ArkHQ-io/ark-python/compare/v0.17.0...v0.18.0)

### Features

* **api:** add Credentials endpoint ([0ff55ca](https://github.com/ArkHQ-io/ark-python/commit/0ff55caabeb38ad0046cf489c28f8dad3caddfc2))
* **api:** add Platform webhooks ([f0a53a7](https://github.com/ArkHQ-io/ark-python/commit/f0a53a79606bece5fd5cf9b2dad7a580b8bae94e))
* **api:** endpoint updates ([0e54a04](https://github.com/ArkHQ-io/ark-python/commit/0e54a042195b1134b7c5cba9ee2ca4b98f35b361))
* **api:** standardization improvements ([b52928d](https://github.com/ArkHQ-io/ark-python/commit/b52928d6147770b7c3a68001dad6d3861ff43967))
* **api:** tenant usage ([09a4d02](https://github.com/ArkHQ-io/ark-python/commit/09a4d02d5acdb3b2a20ca62930e7c644bc5968c9))

## 0.17.0 (2026-02-03)

Full Changelog: [v0.16.0...v0.17.0](https://github.com/ArkHQ-io/ark-python/compare/v0.16.0...v0.17.0)

### Features

* **api:** Add Tenants ([8ba85ac](https://github.com/ArkHQ-io/ark-python/commit/8ba85ac06c8e1d803f2cf5077a1ff99d4655e178))
* **api:** api update ([eed2900](https://github.com/ArkHQ-io/ark-python/commit/eed2900c69e717e346fe6d5d10d95be29771e233))
* **api:** manual updates ([f355920](https://github.com/ArkHQ-io/ark-python/commit/f355920e2008cf0d5990b15c7292483279ee671c))
* **api:** manual updates ([0e5c6fe](https://github.com/ArkHQ-io/ark-python/commit/0e5c6fe1479ca123629e23c842fc3cdf231876e5))
* **api:** manual updates ([e310cbd](https://github.com/ArkHQ-io/ark-python/commit/e310cbdd0ce739190f1094b6ea1c5dd539eb91c4))

## 0.16.0 (2026-01-30)

Full Changelog: [v0.15.0...v0.16.0](https://github.com/ArkHQ-io/ark-python/compare/v0.15.0...v0.16.0)

### Features

* **api:** api update ([56309b8](https://github.com/ArkHQ-io/ark-python/commit/56309b8f34212923562d01dbad53df307d1a6a97))
* **api:** manual updates ([a6fdf54](https://github.com/ArkHQ-io/ark-python/commit/a6fdf54cba7744137502a2e97f9105ef204f4d79))

## 0.15.0 (2026-01-30)

Full Changelog: [v0.14.0...v0.15.0](https://github.com/ArkHQ-io/ark-python/compare/v0.14.0...v0.15.0)

### Features

* **api:** api update ([0f5c166](https://github.com/ArkHQ-io/ark-python/commit/0f5c1666d7c02d1f18096610716be6cb2c39a281))
* **api:** api update ([f128894](https://github.com/ArkHQ-io/ark-python/commit/f128894ef84fffa757424b4b1684f7e4eebf4629))
* **api:** manual updates ([bcc7230](https://github.com/ArkHQ-io/ark-python/commit/bcc72308bfbfd6bfd6cefc6df9e1019637ce1b02))
* **api:** manual updates ([378cd65](https://github.com/ArkHQ-io/ark-python/commit/378cd65aadfd41edd36f4d82ad3ea12d95ec8f0c))
* **api:** manual updates ([edb503c](https://github.com/ArkHQ-io/ark-python/commit/edb503c58439ac4face4260cf1e6794cab79f8bb))
* **client:** add custom JSON encoder for extended type support ([ff51eb2](https://github.com/ArkHQ-io/ark-python/commit/ff51eb229a2eda74e3bc8c16d5f7f43758dc5c31))

## 0.14.0 (2026-01-29)

Full Changelog: [v0.13.0...v0.14.0](https://github.com/ArkHQ-io/ark-python/compare/v0.13.0...v0.14.0)

### Features

* **api:** add usage and SendLimit Headers ([4281980](https://github.com/ArkHQ-io/ark-python/commit/4281980353ff7423dbc6627e37abefee952bc489))
* **api:** api update ([10f496a](https://github.com/ArkHQ-io/ark-python/commit/10f496a29924ecd9bcc93d0551ea8bd29662aa89))
* **api:** domain list improvement ([6929689](https://github.com/ArkHQ-io/ark-python/commit/69296893c13ad8e4f05047f312009e88a8f02830))


### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([f559107](https://github.com/ArkHQ-io/ark-python/commit/f55910772f06f551b98a1ddc7c7dda45fc2176f4))

## 0.13.0 (2026-01-25)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/ArkHQ-io/ark-python/compare/v0.12.0...v0.13.0)

### Features

* **api:** manual updates ([a479b34](https://github.com/ArkHQ-io/ark-python/commit/a479b34c96a0395472f3f5cd0be267de45216762))
* **api:** update email details to include attachments ([041f91e](https://github.com/ArkHQ-io/ark-python/commit/041f91ef9e96ccd47dda255d5a0380ddfece23b0))


### Chores

* **ci:** upgrade `actions/github-script` ([066a689](https://github.com/ArkHQ-io/ark-python/commit/066a6895bd50bea4327966982fca2ea2f94eff8a))

## 0.12.0 (2026-01-23)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/ArkHQ-io/ark-python/compare/v0.11.0...v0.12.0)

### Features

* **api:** fix from in Send raw MIME email ([59d29a6](https://github.com/ArkHQ-io/ark-python/commit/59d29a64079d6e9273f7cde8936b8f2fda4ca48d))
* **api:** improve raw MIME error handling ([0f9682d](https://github.com/ArkHQ-io/ark-python/commit/0f9682db45a4d6014f39df875bc0c56db9420b63))

## 0.11.0 (2026-01-23)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/ArkHQ-io/ark-python/compare/v0.10.0...v0.11.0)

### Features

* **api:** improve raw endpoint ([3ab12b8](https://github.com/ArkHQ-io/ark-python/commit/3ab12b8c773e65632dbc7253e5e37d32883f888a))

## 0.10.0 (2026-01-22)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/ArkHQ-io/ark-python/compare/v0.9.0...v0.10.0)

### Features

* **api:** api update ([53f3037](https://github.com/ArkHQ-io/ark-python/commit/53f30375a1b5dc65cee68df327e9274c4d2757df))
* **api:** api update ([6a8086f](https://github.com/ArkHQ-io/ark-python/commit/6a8086f22354550011274956066a5d022c34b4fa))
* **api:** fix incorrect webhook payload examples ([e78fd9d](https://github.com/ArkHQ-io/ark-python/commit/e78fd9d83b18f6f887faa36eaefa19140283b780))
* **api:** manual updates ([7570f6e](https://github.com/ArkHQ-io/ark-python/commit/7570f6e225f2eca4a9b6398de0fbddb49483a850))

## 0.9.0 (2026-01-22)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/ArkHQ-io/ark-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** improve GET delivery attempts ([104c580](https://github.com/ArkHQ-io/ark-python/commit/104c5800c67096189bffc9d0db6424ec76d9565b))

## 0.8.0 (2026-01-21)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/ArkHQ-io/ark-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** add sandbox domain ([cb771bb](https://github.com/ArkHQ-io/ark-python/commit/cb771bbc1d85d8cae0c449a716457c46c32ee269))

## 0.7.0 (2026-01-20)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/ArkHQ-io/ark-python/compare/v0.6.0...v0.7.0)

### Features

* **api:** add webhook deliveries ([04005c1](https://github.com/ArkHQ-io/ark-python/commit/04005c15bfdb59f935c056beb9ca1b890a7ba887))
* **api:** api update ([b41a63b](https://github.com/ArkHQ-io/ark-python/commit/b41a63b0f283b8a22479d52d768479d4186181a4))
* **api:** api update ([ce1e30e](https://github.com/ArkHQ-io/ark-python/commit/ce1e30eabcd7011b7baed2fe1d16152373b76371))
* **api:** manual updates ([95d0017](https://github.com/ArkHQ-io/ark-python/commit/95d001788faffe7e232c34ec8732b2dd0e68967a))


### Chores

* **internal:** update `actions/checkout` version ([d91b7db](https://github.com/ArkHQ-io/ark-python/commit/d91b7dbbf43b012cfc86cc7e90730fbf066d9480))

## 0.6.0 (2026-01-14)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/ArkHQ-io/ark-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** add metadata ([81dfc11](https://github.com/ArkHQ-io/ark-python/commit/81dfc11bc8a029f7150e4b72919e084963a7bf0a))
* **client:** add support for binary request streaming ([8f5934e](https://github.com/ArkHQ-io/ark-python/commit/8f5934eb54724933c0558002113d8036e02cf39a))

## 0.5.0 (2026-01-13)

Full Changelog: [v0.4.2...v0.5.0](https://github.com/ArkHQ-io/ark-python/compare/v0.4.2...v0.5.0)

### Features

* **api:** manual updates ([8f402b8](https://github.com/ArkHQ-io/ark-python/commit/8f402b8cc60e0d91f69014ba5d4700f6323df0e1))
* **api:** manual updates ([7c37b87](https://github.com/ArkHQ-io/ark-python/commit/7c37b87cd3a04c518041d1be7f1473c138f3bd54))

## 0.4.2 (2026-01-13)

Full Changelog: [v0.4.1...v0.4.2](https://github.com/ArkHQ-io/ark-python/compare/v0.4.1...v0.4.2)

### Chores

* configure new SDK language ([5fb3ec6](https://github.com/ArkHQ-io/ark-python/commit/5fb3ec6ce80d2486e39a89e84b4a16ac486746b7))

## 0.4.1 (2026-01-13)

Full Changelog: [v0.4.0...v0.4.1](https://github.com/ArkHQ-io/ark-python/compare/v0.4.0...v0.4.1)

### Chores

* update SDK settings ([e071de7](https://github.com/ArkHQ-io/ark-python/commit/e071de7d5303bce685aaee2839f7e9b56c84395c))

## 0.4.0 (2026-01-13)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/ArkHQ-io/ark-python/compare/v0.3.0...v0.4.0)

### Features

* **api:** api update ([6c4cc66](https://github.com/ArkHQ-io/ark-python/commit/6c4cc666424e3c1a1aac56ec4536cf4ed3537ace))
* **api:** manual updates ([776e67f](https://github.com/ArkHQ-io/ark-python/commit/776e67f921ea69fb2b7dc33322ebef1a1e05b84d))

## 0.3.0 (2026-01-13)

Full Changelog: [v0.2.0...v0.3.0](https://github.com/ArkHQ-io/ark-python/compare/v0.2.0...v0.3.0)

### Features

* **api:** api update ([ac4c3d7](https://github.com/ArkHQ-io/ark-python/commit/ac4c3d7059fab55e8da4a9f93ffb3413515129fe))
* **api:** manual updates ([17331e6](https://github.com/ArkHQ-io/ark-python/commit/17331e6d8533aef33fb6984754d8ddbca3aaa994))
* **api:** manual updates ([05fbd0c](https://github.com/ArkHQ-io/ark-python/commit/05fbd0c0683d6b40cf3a9b4d07ee21602a938f4d))
* **api:** manual updates ([5d6498c](https://github.com/ArkHQ-io/ark-python/commit/5d6498c0923a34baa3b8cdc6bd70b92eb122c559))
* **api:** manual updates ([07e7603](https://github.com/ArkHQ-io/ark-python/commit/07e76030e28a03aa1c94cd94fc920e47ccabb13b))
* **api:** manual updates ([d03ff5d](https://github.com/ArkHQ-io/ark-python/commit/d03ff5db9843f7561b8825f4070a3d36da434e61))
* **api:** manual updates ([adc040d](https://github.com/ArkHQ-io/ark-python/commit/adc040df33836303bfeb2e1a255cb8ec6bdaea02))
* **api:** manual updates ([600c059](https://github.com/ArkHQ-io/ark-python/commit/600c05906b89ab47a43f8032dd08ad687dc68473))
* **api:** manual updates ([e41f3fc](https://github.com/ArkHQ-io/ark-python/commit/e41f3fc1143d2125115f063c58e8ea75b60e3479))
* **api:** manual updates ([f54f602](https://github.com/ArkHQ-io/ark-python/commit/f54f60266db5c4fd5b5d6cbb076d5ccc43d30ff1))

## 0.2.0 (2026-01-12)

Full Changelog: [v0.1.0...v0.2.0](https://github.com/ArkHQ-io/ark-python/compare/v0.1.0...v0.2.0)

### Features

* **api:** api update ([7690a6d](https://github.com/ArkHQ-io/ark-python/commit/7690a6d828f6adaa02b245f6c88e61aa7846200c))

## 0.1.0 (2026-01-12)

Full Changelog: [v0.0.2...v0.1.0](https://github.com/ArkHQ-io/ark-python/compare/v0.0.2...v0.1.0)

### Features

* **api:** api update ([e46f650](https://github.com/ArkHQ-io/ark-python/commit/e46f650c617e11e1173068ebbb36ac607612e40d))
* **api:** api update ([be470af](https://github.com/ArkHQ-io/ark-python/commit/be470affdcf987f8c0b90aabddee8301593ed41c))

## 0.0.2 (2026-01-12)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/ArkHQ-io/ark-python/compare/v0.0.1...v0.0.2)

### Chores

* configure new SDK language ([c32b083](https://github.com/ArkHQ-io/ark-python/commit/c32b08338547890f0b366a0b6b8f38e4c5289b86))
* update SDK settings ([1fc666c](https://github.com/ArkHQ-io/ark-python/commit/1fc666c5a3d8e8f23ca6f3b9824bf9c2ccc0e4a0))
* update SDK settings ([ddfd3fe](https://github.com/ArkHQ-io/ark-python/commit/ddfd3fec94f3badd64b949699772a74790799951))
