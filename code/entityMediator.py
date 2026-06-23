from code.enemy import Enemy
from code.entity import Entity
from code.player import Player
import pygame


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Entity):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_collision = False
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_collision = True

        if valid_collision:
            if pygame.sprite.collide_mask(ent1, ent2):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        # Procura o Player dentro da lista de entidades ativas
        for ent in entity_list:
            if isinstance(ent, Player):
                ent.score += 1  # Adiciona 1 ponto ao jogador
                break  # Encontrou o player, pode parar o loop

    @staticmethod
    def verify_interation(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)