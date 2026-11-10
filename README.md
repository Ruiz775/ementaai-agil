# EmentaAI — gestão ágil do produto

Repositório de gestão do **EmentaAI**, ERP jurídico web multi-tenant. Aqui ficam o backlog (issues), o board da Sprint (GitHub Projects), os templates e as políticas do time. O código do produto fica em outro repositório.

Trabalho acadêmico — Metodologias Ágeis, UniALFA (Prof. Ranghetti), trabalhos B2-T3 e B2-T4.
Equipe: Gustavo Ruiz (250417) e Murilo Marchiori (14510).

> Os itens descrevem trabalho do produto. Nenhuma issue contém dados reais de clientes ou processos: exemplos usam dados fictícios ou anonimizados.

## Fluxo do board

```
A fazer → Em andamento (WIP 3) → Revisão + CI (WIP 2) → Homologação → Pronto
```

| Coluna | Entra quando | Sai quando |
|---|---|---|
| **A fazer** | O item foi selecionado na Sprint Planning, tem objetivo, critérios de aceitação e estimativa | Alguém assume o item (responsável definido) e há vaga no WIP |
| **Em andamento** (WIP 3) | Responsável definido; cada pessoa tem no máximo 1 item ativo | Pull request aberto com `Closes #n` |
| **Revisão + CI** (WIP 2) | PR aberto e CI rodando | Outra pessoa aprovou o PR e o CI está verde. Reprovado ou CI vermelho: volta para *Em andamento* |
| **Homologação** | PR integrado e deploy em homologação | Checagem de isolamento entre escritórios e de dados pessoais feita; critérios de aceitação conferidos |
| **Pronto** | Definition of Done atendida | — |

**Classe de serviço (raias):** `Padrão` e `Urgente`. A raia **Urgente** aceita só defeito crítico ou incidente de segurança, no máximo 1 item por vez, e quem decide é o PO. Ela entra direto em *Em andamento*, mas passa pela mesma revisão e homologação. Cerca de 20% da capacidade da Sprint fica reservada para ela.

**Bloqueio:** o item continua na coluna em que está, com o campo `Bloqueado = Sim`, um comentário explicando o motivo e quem destrava. Bloqueios são o primeiro assunto da Daily.

## Definition of Done

- [ ] Critérios de aceitação atendidos
- [ ] Testes automatizados verdes (obrigatórios nos módulos Prazos, Financeiro e isolamento de escritórios)
- [ ] Revisão por outra pessoa no PR
- [ ] Checagem de isolamento entre escritórios e de dados pessoais (LGPD)
- [ ] Deploy em homologação conferido
- [ ] Decisões relevantes registradas no item

## Acordos de trabalho (resumo)

- **Registro:** decisão que muda escopo, prioridade ou regra fica escrita na issue. Conversa no chat não vale como registro.
- **Resposta:** menções em issue/PR respondidas em até 24 h em dias úteis. Revisão de PR pedida até 18h é feita até o fim do dia seguinte.
- **Ajuda:** travou por mais de 1 h, pede ajuda no canal do time. Travou por mais de 1 dia, marca `Bloqueado`.
- **Sigilo:** nada de dados reais de clientes em issue, PR, print ou chat.
- **Pares:** obrigatórios em autenticação, isolamento entre escritórios e migrações de banco (label `pares`).
- **Métricas** são do time, nunca por pessoa.

## Labels

| Label | Uso decisório |
|---|---|
| `tipo:funcionalidade`, `tipo:defeito`, `tipo:melhoria`, `tipo:debito-tecnico` | Separar valor novo, correção e saúde técnica no planejamento |
| `bug-do-piloto` | Defeito reportado por escritório-piloto; é a métrica de qualidade revisada a cada Sprint |
| `lgpd` | Item toca dados pessoais ou isolamento entre escritórios: checagem obrigatória na homologação |
| `pares` | Exige programação em pares |
| `precisa-refinar` | Item grande ou ambíguo (13+ pontos ou sem critérios): não entra na Sprint antes do refinamento |
