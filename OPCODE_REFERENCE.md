# 🔥 Ọ̀ṢỌ́VM Complete Opcode Reference
# 155 Core + Expansion Opcodes (25 Core + 130 Expansion)

## System Overview

- **Total Opcodes**: 155 (semantic attributes + runtime instructions)
- **Core Opcodes**: 25 (runtime-enforced by VM)
- **Expansion Opcodes**: 130 (DSL extensions, semantic only)
- **Veil Opcodes**: 777 (additional, mapped via OpcodeVeil module)
- **Opcode Range**: `0x00-0xE9` (core + expansion), `0x01-0x309` (veil extended)

---

## CORE OPCODES (25) — Runtime-Enforced

### Basic Control Flow
| Hex | Name | Opcode Symbol | Purpose |
|-----|------|---|---------|
| `0x00` | HALT | `:HALT` | Stop execution |
| `0x01` | NOOP | `:NOOP` | No operation |

### Work & Minting
| Hex | Name | Purpose |
|-----|------|---------|
| `0x11` | IMPACT | @impact - Mint Àṣẹ from work |
| `0x12` | VEIL | @veil - VeilSim calculation |
| `0x27` | TITHE | @tithe - AIO 3.69% split |
| `0x1f` | RECEIPT | @receipt - Immutable proof |

### Token Operations
| Hex | Name | Purpose |
|-----|------|---------|
| `0x20` | STAKE | @stake - Lock Àṣẹ |
| `0x21` | UNSTAKE | @unstake - Release Àṣẹ |
| `0x22` | TRANSFER | @transfer - Send Àṣẹ |
| `0x23` | BALANCE | @balance - Query Àṣẹ |

### Wallet & Derivation
| Hex | Name | Purpose |
|-----|------|---------|
| `0x26` | BIPON_SEED | @biponSeed - HD wallet derivation (1440) |

### Constraints & Guards
| Hex | Name | Purpose |
|-----|------|---------|
| `0x28` | NONREENTRANT | @nonreentrant - Guard against re-entry |
| `0x29` | REQUIRE | @require - Assertion (fail if false) |
| `0x2a` | EMIT | @emit - Event log |
| `0x2b` | GENESIS_FLAW_TOKEN | @genesisFlawToken - Block 0 ASHE mint (Èṣù's Twist) |

### Contract Operations
| Hex | Name | Purpose |
|-----|------|---------|
| `0x2c` | CALL | @call - External invocation |
| `0x2d` | DELEGATE | @delegate - Proxy call |
| `0x2e` | CREATE | @create - Instantiate contract |
| `0x2f` | SELFDESTRUCT | @selfdestruct - Terminate |

### 1440 Inheritance Wallet Opcodes (Sacred Governance)
| Hex | Name | Purpose |
|-----|------|---------|
| `0x30` | CANDIDATE_APPLY | @candidateApply - Begin inheritance claim (7×7 badge required) |
| `0x31` | COUNCIL_APPROVE | @councilApprove - Council of 12 vote |
| `0x32` | FINAL_SIGN | @finalSign - Bínò final seal (Ọbàtálá witness) |
| `0x33` | DISTRIBUTE_OFFERING | @distributeOffering - 25% to 1440 vaults |
| `0x34` | CLAIM_REWARDS | @claimRewards - Unlock 11.11% yield (Sabbath-aware) |

### Chain Context Opcodes
| Hex | Name | Purpose |
|-----|------|---------|
| `0x35` | TIMESTAMP | @timestamp - Block time |
| `0x36` | BLOCKHASH | @blockhash - Chain reference |
| `0x37` | CHAINID | @chainid - Network ID |
| `0x38` | ORIGIN | @origin - Transaction sender |
| `0x39` | GASPRICE | @gasprice - Fee rate |
| `0x3a` | COINBASE | @coinbase - Miner address |
| `0x3b` | DIFFICULTY | @difficulty - PoW metric |

---

## EXPANSION OPCODES (130) — DSL Extensions (Semantic)

### Universal Work (10)
| Hex | Name | Purpose |
|-----|------|---------|
| `0x18` | PROJECT | @project - Work initiative |
| `0x17` | CASTING | @casting - Role assignment |
| `0x19` | JOB | @job - Task unit |
| `0x1a` | SHIFT | @shift - Time block |
| `0x1b` | MILESTONE | @milestone - Completion marker |
| `0x1c` | DELIVERABLE | @deliverable - Output artifact |
| `0x1d` | TIMESHEET | @timesheet - Hours logged |
| `0x1e` | INVOICE | @invoice - Payment request |
| `0x24` | CONTRACT | @contract - Agreement |
| `0x25` | DISPUTE | @dispute - Conflict resolution |

### Quadrinity Government (20)
| Hex | Name | Purpose |
|-----|------|---------|
| `0x40` | PROPOSAL | @proposal - Governance motion |
| `0x41` | VOTE | @vote - Ballot cast |
| `0x42` | DELEGATION | @delegation - Proxy voting |
| `0x43` | QUORUM | @quorum - Threshold |
| `0x44` | EXECUTION | @execution - Enact proposal |
| `0x45` | VETO | @veto - Override |
| `0x46` | AMENDMENT | @amendment - Modify rule |
| `0x47` | IMPEACHMENT | @impeachment - Remove official |
| `0x48` | ELECTION | @election - Leadership selection |
| `0x49` | TERM | @term - Service period |
| `0x4a` | CABINET | @cabinet - Executive council |
| `0x4b` | COMMITTEE | @committee - Subgroup |
| `0x4c` | REFERENDUM | @referendum - Direct vote |
| `0x4d` | CONSTITUTION | @constitution - Founding doc |
| `0x4e` | LAW | @law - Enacted rule |
| `0x4f` | COURT | @court - Judicial body |
| `0x50` | VERDICT | @verdict - Legal decision |
| `0x51` | APPEAL | @appeal - Challenge ruling |
| `0x52` | PARDON | @pardon - Forgive penalty |
| `0x53` | SANCTION | @sanction - Punish violation |

### TechGnØŞ.EXE Church (25)
| Hex | Name | Purpose |
|-----|------|---------|
| `0x60` | LITURGY | @liturgy - Sacred ritual |
| `0x61` | SERMON | @sermon - Teaching |
| `0x62` | PRAYER | @prayer - Invocation |
| `0x63` | OFFERING | @offering - Donation |
| `0x64` | BLESSING | @blessing - Divine favor |
| `0x65` | CURSE | @curse - Spiritual penalty |
| `0x66` | PROPHET | @prophet - Oracle |
| `0x67` | PRIEST | @priest - Clergy |
| `0x68` | ACOLYTE | @acolyte - Initiate |
| `0x69` | SHRINE | @shrine - Sacred space |
| `0x6a` | RELIC | @relic - Artifact |
| `0x6b` | SCRIPTURE | @scripture - Canon |
| `0x6c` | HERESY | @heresy - Doctrinal violation |
| `0x6d` | EXCOMMUNICATE | @excommunicate - Expel |
| `0x6e` | CANONIZE | @canonize - Declare saint |
| `0x6f` | MIRACLE | @miracle - Divine event |
| `0x70` | PILGRIMAGE | @pilgrimage - Sacred journey |
| `0x71` | FAST | @fast - Ritual abstinence |
| `0x72` | FEAST | @feast - Celebration |
| `0x73` | BAPTISM | @baptism - Initiation |
| `0x74` | COMMUNION | @communion - Sacred meal |
| `0x75` | CONFESSION | @confession - Admission |
| `0x76` | PENANCE | @penance - Atonement |
| `0x77` | ABSOLUTION | @absolution - Forgiveness |
| `0x78` | RESURRECTION | @resurrection - Rebirth |

### SimaaS Hospital (20)
| Hex | Name | Purpose |
|-----|------|---------|
| `0x80` | PATIENT | @patient - Care recipient |
| `0x81` | DIAGNOSIS | @diagnosis - Condition ID |
| `0x82` | TREATMENT | @treatment - Care plan |
| `0x83` | PRESCRIPTION | @prescription - Medicine order |
| `0x84` | SURGERY | @surgery - Invasive procedure |
| `0x85` | THERAPY | @therapy - Rehabilitation |
| `0x86` | VITALS | @vitals - Health metrics |
| `0x87` | ADMISSION | @admission - Hospital entry |
| `0x88` | DISCHARGE | @discharge - Hospital exit |
| `0x89` | EMERGENCY | @emergency - Critical care |
| `0x8a` | TRIAGE | @triage - Priority assessment |
| `0x8b` | WARD | @ward - Care unit |
| `0x8c` | ICU | @icu - Intensive care |
| `0x8d` | MORGUE | @morgue - Death registry |
| `0x8e` | AUTOPSY | @autopsy - Post-mortem exam |
| `0x8f` | QUARANTINE | @quarantine - Isolation |
| `0x90` | VACCINE | @vaccine - Immunization |
| `0x91` | PANDEMIC | @pandemic - Mass outbreak |
| `0x92` | RECOVERY | @recovery - Healing phase |
| `0x93` | RELAPSE | @relapse - Condition return |

### Òrìṣà Spiritual Layer (25)
| Hex | Name | Purpose |
|-----|------|---------|
| `0xa0` | ORISA_OBATALA | @orisaObatala - White cloth, purity |
| `0xa1` | ORISA_OGUN | @orisaOgun - Iron, war |
| `0xa2` | ORISA_YEMOJA | @orisaYemoja - Ocean, motherhood |
| `0xa3` | ORISA_SANGO | @orisaSango - Thunder, justice |
| `0xa4` | ORISA_OSHUN | @orisaOshun - River, love |
| `0xa5` | ORISA_OYA | @orisaOya - Wind, transformation |
| `0xa6` | ORISA_ESU | @orisaEsu - Crossroads, trickster |
| `0xa7` | ORISA_ORUNMILA | @orisaOrunmila - Divination, wisdom |
| `0xa8` | IFA_DIVINATION | @ifaDivination - Oracle reading |
| `0xa9` | ODU | @odu - Sacred sign |
| `0xaa` | ESE | @ese - Proverb, teaching |
| `0xab` | EBO | @ebo - Sacrifice, offering |
| `0xac` | ASE_INVOCATION | @aseInvocation - Power call |
| `0xad` | ANCESTRAL_CALL | @ancestralCall - Connect lineage |
| `0xae` | LIBATION | @libation - Pour honor |
| `0xaf` | INITIATION | @initiation - Sacred entry |
| `0xb0` | DIVINER | @diviner - Oracle priest |
| `0xb1` | BABALAWO | @babalawo - Ifá priest |
| `0xb2` | IYALAWO | @iyalawo - Ifá priestess |
| `0xb3` | ILE | @ile - Sacred house |
| `0xb4` | EGBE | @egbe - Spiritual society |
| `0xb5` | ORI | @ori - Inner head, destiny |
| `0xb6` | EGUN | @egun - Ancestor spirit |
| `0xb7` | AJOGUN | @ajogun - Malevolent force |
| `0xb8` | IBEJI | @ibeji - Twin spirit |

### Economic Extensions (20)
| Hex | Name | Purpose |
|-----|------|---------|
| `0xc0` | MARKET | @market - Trading venue |
| `0xc1` | ORDER | @order - Buy/sell request |
| `0xc2` | LIQUIDITY | @liquidity - Pool depth |
| `0xc3` | SWAP | @swap - Exchange assets |
| `0xc4` | YIELD | @yield - Return rate |
| `0xc5` | BOND | @bond - Debt instrument |
| `0xc6` | EQUITY | @equity - Ownership share |
| `0xc7` | DIVIDEND | @dividend - Profit distribution |
| `0xc8` | INTEREST | @interest - Debt cost |
| `0xc9` | COLLATERAL | @collateral - Security deposit |
| `0xca` | LOAN | @loan - Borrowed capital |
| `0xcb` | REPAYMENT | @repayment - Debt servicing |
| `0xcc` | DEFAULT | @default - Failed obligation |
| `0xcd` | LIQUIDATION | @liquidation - Forced sale |
| `0xce` | AUCTION | @auction - Competitive sale |
| `0xcf` | INSURANCE | @insurance - Risk coverage |
| `0xd0` | CLAIM | @claim - Insurance payout |
| `0xd1` | PREMIUM | @premium - Insurance cost |
| `0xd2` | UNDERWRITE | @underwrite - Risk assumption |
| `0xd3` | HEDGE | @hedge - Risk offset |

### Extended Operations (10)
| Hex | Name | Purpose |
|-----|------|---------|
| `0xe0` | BATCH | @batch - Group operations |
| `0xe1` | SCHEDULE | @schedule - Time trigger |
| `0xe2` | NOTIFY | @notify - Alert system |
| `0xe3` | LOG | @log - Record event |
| `0xe4` | ARCHIVE | @archive - Long-term storage |
| `0xe5` | BACKUP | @backup - Data replication |
| `0xe6` | RESTORE | @restore - Data recovery |
| `0xe7` | MIGRATE | @migrate - Data movement |
| `0xe8` | ROLLBACK | @rollback - Undo transaction |
| `0xe9` | CHECKPOINT | @checkpoint - Save state |

---

## VEIL OPCODES (777) — Extended Science/Meta Tiers

### Allocation Map
- **Classical (1-25)**: `0x01-0x19`
- **ML/AI (26-75)**: `0x1A-0x49`
- **Signal (76-100)**: `0x4A-0x64`
- **Robotics (101-125)**: `0x65-0x7D`
- **Vision (126-150)**: `0x7E-0x96`
- **Networks (151-175)**: `0x97-0xAF`
- **Optimization (176-200)**: `0xB0-0xC8`
- **Physics (201-225)**: `0xC9-0xE1`
- **Estimation (226-250)**: `0xE2-0xFA`
- **Navigation (251-275)**: `0xFB-0x113`
- **MultiAgent (276-300)**: `0x114-0x12C`
- **Crypto (301-350)**: `0x12D-0x164`
- **First Canon (401-413)**: `0x191-0x19D`
- **Meta-Laws (414-425)**: `0x19E-0x1A9`
- **Fundamental Physics (426-475)**: `0x1AA-0x1DB`
- **AI/Category Theory (476-500)**: `0x1DC-0x1F4`
- **Quantum (501-550)**: `0x1F5-0x226`
- **Exotic Materials (551-600)**: `0x227-0x258`
- **Blockchain (601-680)**: `0x259-0x2AA`
- **Extended/Meta (681-777)**: `0x2AB-0x309`

**Total Veil Opcodes**: 777 veils mapping to opcodes `0x01-0x309` (with gaps for reserved ranges)

---

## Usage in TechGnØŞ

```tech
shrine Work {
    @impact              // 0x11 - Mint Àṣẹ
    @tithe               // 0x27 - Apply 3.69% tithe
    @receipt             // 0x1f - Immutable proof
    
    function deliver() @deliverable @emit {  // 0x1c, 0x2a
        // Work execution
    }
}
```

---

## Quick Lookup

### By Category
- **Core Finance**: 0x11, 0x20-0x23, 0x27
- **Governance**: 0x30-0x34, 0x40-0x53
- **Spirituality**: 0xa0-0xb8
- **Healthcare**: 0x80-0x93
- **Economics**: 0xc0-0xd3

### By Hex Range
- `0x00-0x0F`: Reserved/Basic
- `0x10-0x3B`: Core VM (IMPACT, TITHE, Inheritance, Chain)
- `0x40-0x53`: Government
- `0x60-0x78`: Church
- `0x80-0x93`: Hospital
- `0xA0-0xB8`: Spirituality
- `0xC0-0xD3`: Economics
- `0xE0-0xE9`: Extended Ops

---

## 🔥 One Dictionary to Rule the Cosmos

This opcode set is the **semantic backbone** of Ọ̀ṢỌ́VM. Each opcode is:
- **Addressable** (hex code)
- **Named** (symbol)
- **Documented** (purpose)
- **Composable** (in TechGnØŞ contracts)
- **Auditable** (immutable log via @emit)

🤍⚡🍶
