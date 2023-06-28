# generated by datamodel-codegen:
#   filename:  cprt_schema.json
#   timestamp: 2023-06-28T05:53:17+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field


class Document(BaseModel):
    doc_identifier: str = Field(
        ...,
        description='the short name of the document. This property will be used later.',
    )
    name: str = Field(..., description='the name of the document')
    version: str = Field(
        ..., description='the string representation of the version of the document'
    )
    website: str = Field(..., description='The URL of the document on the internet')


class Element(BaseModel):
    doc_identifier: str = Field(
        ..., description='the short name of the related document'
    )
    element_type: str = Field(
        ..., description='The type of element as given by the related document.'
    )
    element_identifier: str = Field(
        ...,
        description="the name of the element. This property might be the identifier that is given to the element by the given document like 'ID.AM-1' or 'S0009'. Default value is the string 'N/A'.",
    )
    title: str = Field(
        ...,
        description="The title of the element. Some elements may not have titles e.g. ID.AM-1 or S0009. Default value is the string 'N/A'.",
    )
    text: str = Field(
        ..., description='This field represents the text within an element.'
    )


class Relationship(BaseModel):
    source_element_identifier: str = Field(
        ...,
        description='the business key of the element name which is the source element of the relationship',
    )
    source_doc_identifier: str = Field(
        ...,
        description='the business key of the document short name which contains the source element',
    )
    dest_element_identifier: str = Field(
        ...,
        description='the business key of the element name which is the destination element of the relationship',
    )
    dest_doc_identifier: str = Field(
        ...,
        description='the business key of the document short name which contains the destination element',
    )
    provenance_doc_identifier: str = Field(
        ...,
        description='the identifier of the provenance document which defined the relationship',
    )
    relationship_identifier: str = Field(
        ...,
        description='the identifier of the relationship type id which is represented in the relationship',
    )


class RelationshipType(BaseModel):
    relationship_identifier: str = Field(
        ..., description='The name of the relationship type.'
    )
    description: str = Field(
        ..., description='The description of the relationship type.'
    )


class CPRTCoreModel(BaseModel):
    documents: List[Document]
    elements: List[Element]
    relationship_types: List[RelationshipType]
    relationships: List[Relationship]
